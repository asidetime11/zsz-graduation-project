from django.urls import path

from .views import (
    create_doc_page,
    create_document,
    document_list_page,
    export_documents,
    export_page,
    get_document,
)

urlpatterns = [
    path("", document_list_page, name="document_list"),
    path("documents/create-page/", create_doc_page, name="create_doc_page"),
    path("documents/create/", create_document, name="create_document"),
    path("documents/<int:doc_id_path>/", get_document, name="get_document"),
    path("export/", export_documents, name="export_documents"),
    path("export-page/", export_page, name="export_page"),
]
