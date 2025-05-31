
accent_mapping = {'england' : 0,
'us' : 1,
'canada' : 2,
'australia' : 3,
'indian' : 4,
'scotland' : 5,
'ireland' : 6,
'african' : 7,
'malaysia' : 8,
'newzealand' : 9,
'southatlandtic' : 10,
'bermuda' : 11,
'philippines' : 12,
'hongkong' : 13,
'wales' : 14,
'singapore' : 15
}

prompt = '''
You are an English transcription assistant.

Task:
1. Transcribe the given audio file in English.
2. Provide a brief summary of the transcription.

Format your response strictly as a JSON object with two fields:
{
  "transcription": "<full transcription text>",
  "summary": "<brief summary>"
}

Do not include any text outside the JSON object.
'''
