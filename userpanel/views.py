from django.http import Http404
from rest_framework import generics, permissions, status, views
from rest_framework.response import Response
from rest_framework import viewsets

from adminpanel.models import DocumentModel, Job, JobQuestion
from adminpanel.serializers import DocumentSerializer
from userpanel.models import *
from userpanel.serializers import *
from rest_framework.decorators import action
from adminpanel.serializers import *
from .utils import decryptDoc, encryptDoc
import requests
import os

# Create your views here.

class ProfileDocumentView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProfileDocumentSerializer
    queryset = ProfileDocumentModel.objects.all()
    def get(self, request):
        
        serializer = self.serializer_class(data=request.data)
        
        # if not serializer.is_valid():
        #     return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
        
        data = dict()
        data["user"]= request.user
        r = request.user
        doc = DocumentModel.objects.filter(user=r)
        doc1 = DocumentModel.objects.get(user=r)
        doc_data =DocumentSerializer(doc, many = True).data
        cus = CustomDocumentUploadModel.objects.filter(user=r)
        cus_data = CustomDocumentSerializer(cus, many = True).data
        data["NAD_Documents"]= doc1
        """uncomment in post request"""
        # custom_document = ProfileDocumentModel.objects.create(**data)
        # custom_document.save()
        view_doc= dict()
        view_doc["user"]= request.user.id
        view_doc["NAD_Document"]= [*doc_data]
        view_doc["Custom_Document"]= [*cus_data]
        # print(data)
        return Response(
            view_doc,
            status=status.HTTP_200_OK
        )
        
    
class CustomDocumentView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CustomDocumentSerializer
    queryset =CustomDocumentUploadModel.objects.all()
    
    """View all documents of CustomDocument"""
    
    def get_object(self, pk):
        try:
            return CustomDocumentUploadModel.objects.get(pk=pk)
        except CustomDocumentUploadModel.DoesNotExist:
            raise Http404
        
    def get(self, pk):
        form = self.get_object(pk)
        serializer = CustomDocumentSerializer(form)
        return Response(serializer.data)
    
    def get(self, request, format=None, **kwargs):
        form = CustomDocumentUploadModel.objects.all()
        serializer = CustomDocumentSerializer(form, many=True)
        return Response(serializer.data,status = status.HTTP_200_OK)
    
    """Add documents to profile"""
    
    def post(self, request, format=None):
        serializer = CustomDocumentSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        serializer.save(user=request.user)
        
        return Response(
            {"success": "File uploaded successfully"},
            status=status.HTTP_201_CREATED
        )

class RecentUpload(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProfileDocumentSerializer
    queryset = ProfileDocumentModel.objects.all()

    def get(self, request):
        
        data = dict()
        data["user"]= request.user
        r = request.user

        cus = CustomDocumentUploadModel.objects.filter(user=r).order_by('-upload_time')
        cus_data = CustomDocumentSerializer(cus , many = True).data
        view_doc= dict()
        
        view_doc["Recent Upload"]= [*cus_data]
        len_view_doc = len(view_doc["Recent Upload"])
        # print(len_view_doc)
        if len_view_doc<=5:
        
            return Response(
                view_doc,
                status=status.HTTP_200_OK
            )
        
        else:
            final_doc= list()
            for x in view_doc["Recent Upload"]:
                final_doc.append(x)
                if len(final_doc) ==5:
                    break

            return Response(
                final_doc,
                status=status.HTTP_200_OK
            )
            
# class SubmitAnswer(generics.GenericAPIView):
#     permission_classes = [permissions.IsAuthenticated]
    
class SubmitFileQuestionView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = JobSubmitFileQuestion.objects.all()
    action_serializers = {
        'job': JobSubmitFileQuestionSerializer,
        'college': SubmitFileQuestionSerializer
    }
    
    def get_serializer_class(self):
        if hasattr(self, 'action_serializers'):
            return self.action_serializers.get(self.action, self.serializer_class)

        return super(SubmitFileQuestionView, self).get_serializer_class()
    
    @action(detail=False, methods=['post'],url_path='college')
    def college(self, request, format=None):
        serializer = self.get_serializer_class()(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['post'],url_path='job')
    def job(self, request, format=None):
        serializer = self.get_serializer_class()(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SubmitTextQuestionView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = JobSubmitTextQuestion.objects.all()
    action_serializers = {
        'job': JobSubmitTextQuestionSerializer,
        'college': SubmitTextQuestionSerializer
    }
    
    def get_serializer_class(self):
        if hasattr(self, 'action_serializers'):
            return self.action_serializers.get(self.action, self.serializer_class)

        return super(SubmitTextQuestionView, self).get_serializer_class()
    
    @action(detail=False, methods=['post'],url_path='college')
    def college(self, request, format=None):
        serializer = self.get_serializer_class()(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['post'],url_path='job')
    def job(self, request, format=None):
        serializer = self.get_serializer_class()(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class SubmitPreVerifiedQuestionView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = SubmitPreVerifiedQuestion.objects.all()
    action_serializers = {
        'job': JobSubmitPreVerifiedQuestionSerializer,
        'college': SubmitPreVerifiedQuestionSerializer
    }
    
    def get_serializer_class(self):
        if hasattr(self, 'action_serializers'):
            return self.action_serializers.get(self.action, self.serializer_class)

        return super(SubmitPreVerifiedQuestionView, self).get_serializer_class()

    @action(detail=False, methods=['post', 'get'],url_path='college')
    def college(self, request, *args, **kwargs):
        serializer = self.get_serializer_class()(data=request.data)
        if request.method == 'GET':
            answer = SubmitPreVerifiedQuestion.objects.all()
            serializer = self.get_serializer_class()(answer, many=True)
            return Response(serializer.data,status = status.HTTP_200_OK)
            
        if request.method == 'POST':
            docs = DocumentModel.objects.get(user= request.user)
            submitpre = SubmitPreVerifiedQuestion(user= request.user)
            docs_data = DocumentSerializer(docs).data
            question = Question.objects.get(id = request.data['question'])
            
            if not serializer.is_valid():
                return Response(serializer.errors)
            data = serializer.data
            for key,value in docs_data.items():
                if str(question.title).lower() == str(key).lower():
                    submitpre.file_id = value
                    data['file_id'] = value
            submitpre.user= request.user
            submitpre.title = data['title']
            submitpre.question = Question.objects.get(id = data['question'])
            submitpre.save()
            return Response(data, status=status.HTTP_201_CREATED)
    
    @action(detail=False, methods=['post'],url_path='job')
    def job(self, request, *args, **kwargs):
        docs = DocumentModel.objects.get(user= request.user)
        submitpre = JobSubmitPreVerifiedQuestion(user= request.user)
        docs_data = DocumentSerializer(docs).data
        question = JobQuestion.objects.get(id = request.data['question'])
        serializer = self.get_serializer_class()(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        data = serializer.data
        for key,value in docs_data.items():
            if str(question.title).lower() == str(key).lower():
                submitpre.file_id = value
                data['file_id'] = value
        submitpre.user= request.user
        submitpre.title = data['title']
        submitpre.question = JobQuestion.objects.get(id = data['question'])
        submitpre.save()
        return Response(data, status=status.HTTP_201_CREATED)
       
    
class UploadDocumentViewset(viewsets.ModelViewSet):
    
    permission_classes = [permissions.IsAuthenticated]
    queryset = DocumentModel.objects.all()
    def get_serializer_class(self):
        if hasattr(self, 'action_serializers'):
            return self.action_serializers.get(self.action, self.serializer_class)

        return super(UploadDocumentViewset, self).get_serializer_class()
    
    action_serializers = {
        "adhaar": AdhaarFileSerializer,
        "SSC": SSCSerializer,
        "HSC": HSCSerializer,
        "migration": MigrationCertificateSerializer,
        "JEE marksheet": JEEmarksheetSerializer,
        "JEE allotment letter": JEEallotmentLetterSerializer,
        "disability": DisabilityCertificateSerializer,
        "birth": BirthCertificateSerializer,
        "domicile": DomicileCertificateSerializer,
        "PAN": PANSerializer,
        "passport": PassportSerializer,
        "sports": SportsCertificateSerializer,
        "transfer": TransferCertificateSerializer,
        "caste": CasteCertificateSerializer,
        "income": IncomeCertificateSerializer,
        "medical": MedicalCertificateSerializer,
        "nationality": NationalityCertificateSerializer
    }
    
    def handle_action(self, action_name, request):
        serializer_class = self.action_serializers.get(action_name)
        data = request.data
        
        file = request.FILES['file']
        file = file.read()
        # print(file)
        encoded_data = encryptDoc(file)
        # print(encoded_data['ecryptedDoc'])
        token = os.environ.get('token') 
        ipfs_data = requests.post(url = 'https://api.web3.storage/upload',
                                  headers={'Authorization': 'Bearer ' + token},
                                  data = encoded_data['ecryptedDoc']).json()
        
        data['Private_key'] = encoded_data['privateKey']
        data['IPFS_Key'] = ipfs_data['cid']
        serializer = serializer_class(data=data)
        
        model_name = serializer.Meta.model
        if request.method == 'GET':
            serializer = serializer_class(model_name.objects.all(), many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        

        if serializer.is_valid():
            # serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['post', 'get'], url_path='adhaar')
    def adhaar(self, request, format=None, **kwargs):
        return self.handle_action('adhaar', request)

    @action(detail=False, methods=['post', 'get'], url_path='ssc')
    def SSC(self, request, format=None, **kwargs):
        return self.handle_action('SSC', request)

    @action(detail=False, methods=['post', 'get'], url_path='hsc')
    def HSC(self, request, format=None, **kwargs):
        return self.handle_action('HSC', request)

    @action(detail=False, methods=['post', 'get'], url_path='migration')
    def migration(self, request, format=None, **kwargs):
        return self.handle_action('migration', request)

    @action(detail=False, methods=['post', 'get'], url_path='jee-marksheet')
    def JEE_marksheet(self, request, format=None, **kwargs):
        return self.handle_action('JEE marksheet', request)

    @action(detail=False, methods=['post', 'get'], url_path='jee-allotment-letter')
    def JEE_allotment_letter(self, request, format=None, **kwargs):
        return self.handle_action('JEE allotment letter', request)

    @action(detail=False, methods=['post', 'get'], url_path='disability')
    def disability(self, request, format=None, **kwargs):
        return self.handle_action('disability', request)
    
    @action(detail=False, methods=['post', 'get'], url_path='birth')
    def birth(self, request, format=None, **kwargs):
        return self.handle_action('birth', request)

    @action(detail=False, methods=['post', 'get'], url_path='domicile')
    def domicile(self, request, format=None, **kwargs):
        return self.handle_action('domicile', request)

    @action(detail=False, methods=['post', 'get'], url_path='pan')
    def PAN(self, request, format=None, **kwargs):
        return self.handle_action('PAN', request)

    @action(detail=False, methods=['post', 'get'], url_path='passport')
    def passport(self, request, format=None, **kwargs):
        return self.handle_action('passport', request)

    @action(detail=False, methods=['post', 'get'], url_path='sports')
    def sports(self, request, format=None, **kwargs):
        return self.handle_action('sports', request)

    @action(detail=False, methods=['post', 'get'], url_path='transfer')
    def transfer(self, request, format=None, **kwargs):
        return self.handle_action('transfer', request)

    @action(detail=False, methods=['post', 'get'], url_path='caste')
    def caste(self, request, format=None, **kwargs):
        return self.handle_action('caste', request)

    @action(detail=False, methods=['post', 'get'], url_path='income')
    def income(self, request, format=None, **kwargs):
        return self.handle_action('income', request)

    @action(detail=False, methods=['post', 'get'], url_path='medical')
    def medical(self, request, format=None, **kwargs):
        return self.handle_action('medical', request)

    @action(detail=False, methods=['post', 'get'], url_path='nationality')
    def nationality(self, request, format=None, **kwargs):
        return self.handle_action('nationality', request)
    
class RetrieveDocument(views.APIView):
    
    def post(self,request):
        data = request.data
        private_key = "hey"
        if SSC.objects.get(user = data['user']).IPFS_Key == data['IPFS_Key']:
            private_key = SSC.Private_key
        elif HSC.objects.get(user = data['user']).IPFS_Key == data['IPFS_Key']:
            private_key = HSC.Private_key
        elif AdhaarFile.objects.get(user = data['user']).IPFS_Key == data['IPFS_Key']:
            private_key = AdhaarFile.Private_key
        elif MigrationCertificate.objects.get(user = data['user']).IPFS_Key == data['IPFS_Key']:
            private_key = MigrationCertificate.Private_key
        elif JEEmarksheet.objects.get(user = data['user']).IPFS_Key == data['IPFS_Key']:
            private_key = JEEmarksheet.Private_key
        elif JEEallotmentLetter.objects.get(user = data['user']).IPFS_Key == data['IPFS_Key']:
            private_key = JEEallotmentLetter.Private_key
        elif DisabilityCertificate.objects.get(user = data['user']).IPFS_Key == data['IPFS_Key']:
            private_key = DisabilityCertificate.Private_key
        elif BirthCertificate.objects.get(user = data['user']).IPFS_Key == data['IPFS_Key']:
            private_key = BirthCertificate.Private_key
        elif DomicileCertificate.objects.get(user = data['user']).IPFS_Key == data['IPFS_Key']:
            private_key = DomicileCertificate.Private_key
        elif PAN.objects.get(user = data['user']).IPFS_Key == data['IPFS_Key']:
            private_key = PAN.Private_key
        elif Passport.objects.get(user = data['user']).IPFS_Key == data['IPFS_Key']:
            private_key = Passport.Private_key
        elif SportsCertificate.objects.get(user = data['user']).IPFS_Key == data['IPFS_Key']:
            private_key = SportsCertificate.Private_key
        elif TransferCertificate.objects.get(user = data['user']).IPFS_Key == data['IPFS_Key']:
            private_key = TransferCertificate.Private_key
        elif CasteCertificate.objects.get(user = data['user']).IPFS_Key == data['IPFS_Key']:
            private_key = CasteCertificate.Certificate
        elif IncomeCertificate.objects.get(user = data['user']).IPFS_Key == data['IPFS_Key']:
            private_key = IncomeCertificate.objects.get(user = data['user']).Private_key
        elif MedicalCertificate.objects.get(user = data['user']).IPFS_Key == data['IPFS_Key']:
            private_key = MedicalCertificate.Private_key
        elif NationalityCertificate.objects.get(user = data['user']).IPFS_Key == data['IPFS_Key']:
            private_key = NationalityCertificate.Private_key
            
        doc = requests.get(url = "https://"+data['IPFS_Key']+".ipfs.w3s.link").json()
        return_data = decryptDoc(doc, private_key)
            
        return Response(return_data['decryptedDoc'], status=status.HTTP_200_OK)      
    

        
    

