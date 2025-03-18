"""
Simple adapter that outputs two extended m3u8 files from a Timeline for audio and video tracks.

Ex:
#EXTM3U
#PLAYLIST: {input_otio.name}
#EXTINF:{duration},{display_title}
item.media_reference
#EXTINF:{duration},{display_title}
item.media_reference
#EXTINF:{duration},{display_title}
item.media_reference
"""

import opentimelineio as otio
import opentimelineio.exceptions
import os
from otio_m3u8_adapter.adapters.m3u8_adapter import write_tracks_list_to_string

def write_to_file(input_otio, filepath):
    """
    Write two m3u8 files to the directory, for audio tracks, and video tracks, in clip
    start time order.
    """
    # Create the directory using filepath
    if os.path.exists(filepath):
        raise opentimelineio.exceptions.OTIOError(f"'{filepath}' exists, will not overwrite.")
#    if not os.path.exists(os.path.dirname(filepath)):
#        raise exceptions.OTIOError("Directory '{}' does not exist, cannot create '{}'.".format(os.path.dirname(filepath), filepath))
#    if not os.path.isdir(os.path.dirname(filepath)):
#        raise exceptions.OTIOError("'{}' is not a directory, cannot create '{}'.".format(os.path.dirname(filepath), filepath))
    os.mkdir(filepath)
    
    # Split out the audio and video tracks as two separate m3u8 tracks.
    playlist_filepath = os.path.join(filepath, "audio.m3u8")
    with open(playlist_filepath, 'w') as file_handle:
        file_handle.write(write_tracks_list_to_string(f"Audio tracks of {input_otio.name}", input_otio.audio_tracks()))
    playlist_filepath = os.path.join(filepath, "video.m3u8")
    with open(playlist_filepath, 'w') as file_handle:
        file_handle.write(write_tracks_list_to_string(f"Video tracks of {input_otio.name}", input_otio.video_tracks()))
        
