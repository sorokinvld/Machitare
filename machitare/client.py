import socket
import threading
import pyaudio
import simpleaudio as sa
import streaming_pb2 
import time

# Global settings
SERVER_ADDRESS = ('server_address', 5000)  # Replace with your server's address and port

# Audio settings
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024

# Initialize PyAudio
audio = pyaudio.PyAudio()

# Function to capture and send audio
def capture_and_send_audio():
    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(SERVER_ADDRESS)

    while True:
        data = stream.read(CHUNK, exception_on_overflow=False)
        audio_chunk = streaming_pb2.AudioChunk(data=data, sampleRate=RATE, bitDepth=16, channels=CHANNELS)
        
        stream_data = streaming_pb2.StreamData()
        stream_data.audio.CopyFrom(audio_chunk)
        
        client_socket.sendall(stream_data.SerializeToString())

# Function to receive and play audio
def receive_and_play_audio():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(SERVER_ADDRESS)
    
    while True:
        # Assuming the server sends audio data back in the same format
        data = client_socket.recv(4096)
        stream_data = streaming_pb2.StreamData()
        stream_data.ParseFromString(data)
        
        if stream_data.HasField('audio'):
            # Play audio
            play_obj = sa.play_buffer(stream_data.audio.data, CHANNELS, 2, RATE)
            play_obj.wait_done()
        elif stream_data.HasField('event'):
            # Print event message to console
            print(f"Event: {stream_data.event.type}, Content: {stream_data.event.content}")

# Start threads for audio capture and playback
def start_client():
    threading.Thread(target=capture_and_send_audio, args=()).start()
    threading.Thread(target=receive_and_play_audio, args=()).start()

start_client()
