import tkinter as tk
import yt_dlp as youtube_dl
from tkinter import messagebox
import os

def descargar_audio():
    url = url_entry.get().strip()
    path = path_entry.get().strip()
    if not url or not path:
        messagebox.showerror("Error", "Por favor, introduce la URL y la ruta.")
        return
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'{path}/%(title)s.%(ext)s',
            'ffmpeg_location': os.path.join(os.getcwd(), 'ffmpeg', 'ffmpeg.exe'),  # Ruta a ffmpeg 
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("\n Descarga completada!")
    except Exception as e:
        print(f"\n Ha ocurrido un error: {e}")

def descargar_video():
    url = url_entry.get().strip()
    path = path_entry.get().strip()
    if not url or not path:
        messagebox.showerror("Error", "Por favor, introduce la URL y la ruta.")
        return
    try:
        ydl_opts = { 
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': f'{path}/%(title)s.%(ext)s',
            'merge_output_format': 'mp4',
            'ffmpeg_location': os.path.join(os.getcwd(), 'ffmpeg', 'ffmpeg.exe'),  # Ruta a ffmpeg 
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("\n Descarga completada!")
    except Exception as e:
        print(f"\n Ha ocurrido un error: {e}")

root = tk.Tk()
root.title("Descargador de videos de YouTube")

# Crear y colocar los widgets
tk.Label(root, text="URL del video de YouTube:").grid(row=0, column=0, padx=10, pady=10)
url_entry = tk.Entry(root, width=50)
url_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Ruta para guardar el video:").grid(row=1, column=0, padx=10, pady=10)
path_entry = tk.Entry(root, width=50)
path_entry.grid(row=1, column=1, padx=10, pady=10)

download_button = tk.Button(root, text="Descargar audio", command=descargar_audio)
download_button.grid(row=2, column=1, columnspan=1, pady=10)

download_button = tk.Button(root, text="Descargar video", command=descargar_video)
download_button.grid(row=3, column=1, columnspan=2, pady=10)

# Iniciar el bucle principal de la aplicación
root.mainloop()