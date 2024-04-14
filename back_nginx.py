from pyngrok import ngrok


# Set up a HTTP tunnel on port 8000
tunnel = ngrok.connect(8000, "http")
public_url = tunnel.public_url

print("Public URL:", public_url)
# Keep the tunnel open until interrupted
try:
    input("Press Enter to exit...")
except KeyboardInterrupt:
    ngrok.disconnect(public_url)
