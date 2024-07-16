Kinda working, thread issue.

Next is to refecator sound out 

> joystick | fingertips | oscillators | speaker

This requires defining
1) an oscilator control protocol, eg Open Sound Control
2) joystick mapping to osc
3) fingertips mapping osc 
4) audio format 

For 1:
https://ccrma.stanford.edu/groups/osc/index.html

For 2, 3:
Use LLM

For 4:
Easiest is 16 bit stereo, E.G. RTAUDIO_SINT24 See: 
https://web.mit.edu/carrien/Public/speechlab/marc_code/ADAPT_VC/rtaudio/doc/html/index.html

Possible typedef unsigned long RtAudioFormat:
  static const RtAudioFormat  RTAUDIO_SINT8;   // Signed 8-bit integer
  static const RtAudioFormat  RTAUDIO_SINT16;  // Signed 16-bit integer
  static const RtAudioFormat  RTAUDIO_SINT24;  // Signed 24-bit integer (32bit) 
  static const RtAudioFormat  RTAUDIO_SINT32;  // Signed 32-bit integer
  static const RtAudioFormat  RTAUDIO_FLOAT32; // 32-bit float +/- 1.0
  static const RtAudioFormat  RTAUDIO_FLOAT64; // 64-bit double +/- 1.0
