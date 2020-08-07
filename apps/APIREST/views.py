from django.shortcuts import render
from django.http import HttpResponse
from wsgiref.util import FileWrapper
import base64
from rest_framework.parsers import FileUploadParser
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

import nbformat
import argparse
from ..utils import *

def isNoteBook(file_name):
    print(file_name[-5:])
    if file_name[-5:] == 'ipynb':
        return True
    else:
        return False

class JupyterToPDF(APIView):

    parser_classes = (MultiPartParser,FormParser,FileUploadParser,)

    def post(self, request, format=None):
        print(request.FILES)
        if len(request.FILES):
            if 'file' in request.FILES.keys():
                file = request.FILES['file']
                if not isNoteBook(file.name):
                    return Response({"statuss":False}, status=status.HTTP_400_BAD_REQUEST)
                file_path = "./files/" + file.name
                file_path_save = "../files/" + file.name
                newFile = open(file_path, "wb")
                newFile.write(file.read())
                notebook = nbformat.read(file_path, as_version = 4)
                Exporter = PDFExporter()
                Exporter.set__outputFileName(file_path_save)
                pdfFile = Exporter.from_notebook_node(notebook)
                file_path_pdf = "./files/" + file.name + ".pdf"
                file_path_pdf_attachment = "./files/" + file.name + "-with-attachment.pdf"
                file_name_response = file.name + ".pdf"
                output = open(file_path_pdf_attachment, "rb")

                if False:
                    response = HttpResponse(FileWrapper(output), content_type='application/pdf')
                    response['Content-Disposition'] = 'attachment; filename="'+ file_name_response +'"'
                    return response
                else:
                    encoded_string = base64.b64encode(output.read())
                    return Response({"statuss":True, "filename": file_name_response, "base64file": encoded_string}, status=status.HTTP_200_OK)
            else:
                return Response({"statuss":False}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"statuss":False}, status=status.HTTP_400_BAD_REQUEST)