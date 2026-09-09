import qrcode

def generate_upi_qr(upi_id, name, amount=None, note=None, filename="upi_qr.png"):
    """
    Generates a UPI payment QR code and saves it as an image.
    
    Parameters:
    - upi_id: UPI ID of the receiver
    - name: Name of the payee
    - amount: Optional payment amount
    - note: Optional payment note
    - filename: Output image filename
    """

    # Start forming the UPI URI
    upi_uri = f"upi://pay?pa={upi_id}&pn={name}"

    if amount:
        upi_uri += f"&am={amount}"
    if note:
        upi_uri += f"&tn={note}"

    # Generate and save the QR code
    qr = qrcode.make(upi_uri)
    qr.save(filename)
    print(f"UPI QR code saved as '{filename}'")

    return upi_uri  

if __name__ == "__main__":
    print("=== QRverse: UPI QR Code Generator ===")
    
    upi_id = input("Enter UPI ID: ").strip()
    name = input("Enter receiver name: ").strip()
    amount = input("Enter amount (optional): ").strip()
    note = input("Enter note (optional): ").strip()

    # Treat empty strings as None
    amount = amount if amount else None
    note = note if note else None

    generate_upi_qr(upi_id, name, amount, note)
