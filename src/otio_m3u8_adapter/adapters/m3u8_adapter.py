"""
Super simple adapter that outputs an extended m3u8 formatted string from a Timeline.

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

#import json
import opentimelineio as otio

# def read_from_string(input_str):
#     data = json.loads(input_str)
#     timeline_name = data['timeline']['name']
#     track_name = data['track']['name']
#     clip_data = data['clip']
#     timeline = otio.schema.Timeline(timeline_name)
#     track = otio.schema.Track(track_name)
#     clip = otio.schema.Clip(
#         clip_data['name'],
#         source_range=otio.opentime.TimeRange(
#             otio.opentime.RationalTime(clip_data['in'], clip_data['rate']),
#             otio.opentime.RationalTime(clip_data['out'], clip_data['rate'])
#         )
#     )
#     timeline.tracks.append(track)
#     track.append(clip)
#     return timeline

def clip_start(clip):
    return clip.source_range.start_time

def write_tracks_list_to_string(playlist_name, tracks_list):
    """
    Turn a list of Tracks into a very simple M3U8 file.
    """
    m3u8_playlist =  "#EXTM3U\n"
    m3u8_playlist += f"#PLAYLIST: {playlist_name}\n"
    # Merge the clips in the list of tracks to a single list of clips, sorted on the start
    # time of each audio clip, and output as a single m3u8 file.
    all_clips = []
    for track in tracks_list:
        all_clips.extend(track.find_clips())
    for item in sorted(all_clips, key=clip_start):
        if clip.media_reference is not None:
            # start = otio.opentime.to_seconds(item.source_range.start_time)
            # TODO Should this be rounded to the nearest second?
            duration = otio.opentime.to_seconds(item.source_range.duration)
            display_title = item.name
            m3u8_playlist += f"#EXTINF:{duration},{display_title}\n"
            m3u8_playlist += item.media_reference.target_url + "\n"
    return m3u8_playlist

def write_to_string(input_otio):
    """
    Turn a single track timeline into a very simple M3U8 file.
    """
    if len(input_otio.tracks) != 1:
        raise Exception("This adapter does not support multiple tracks.")
    return write_tracks_list_to_string(input_otio.name, [input_otio.tracks[0]])
