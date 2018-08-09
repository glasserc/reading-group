from datetime import datetime
from django.shortcuts import render_to_response, get_object_or_404
from . import models

def show(request, transcript_id):
    transcript = get_object_or_404(models.Transcript, pk=transcript_id)
    now = datetime.utcnow()
    return render_to_response(
        'transcript/show.html',
        context=dict(transcript=transcript,
                     student=transcript.student,
                     now=now,
        ))
