from rest_framework import views, permissions
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response

from api.orchestrator import orchestrator


class IngestView(views.APIView):
    parser_classes = (FileUploadParser,)
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, filename, format=None):
        try:
            orchestrator(file_name=filename, file_patch=request.data['file'], user=request.user)
            return Response(status=204)
        except Exception as e:
            return Response({'error': str(e)}, status=400)