from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import DocumentForm
from .models import Document
import cv2
import numpy as np
from django.conf import settings
from PIL import Image
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def index(request):
	return render(request, 'image_app/index.html')
	
	# document_list = Document.objects.all().order_by('-id')

	# if request.method == 'POST':
	# 	form = DocumentForm(request.POST, request.FILES)
	# 	if form.is_valid():
	# 		photo_data = form.save()
	# 		max_id = Document.objects.latest('id').id
	# 		max_id_str = str(max_id)
	# 		obj = Document.objects.get(id = max_id)
	# 		input_path = settings.BASE_DIR + obj.photo.url
	# 		output_path = settings.BASE_DIR + "/media/output/" + max_id_str + ".jpg"
	# 		output_path_gif = settings.BASE_DIR + "/media/output/" + max_id_str + ".gif"
	# 		img = cv2.imread(input_path)
	# 		if obj.description == "グレースケール":
	# 			img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	# 			cv2.imwrite(output_path, img_gray)
	# 			output_path = output_path.replace("/Users/suehiro/1pro/Django/image_app/ImageService/media", "")
	# 			photo_data.output = output_path
	# 			photo_data.save()
	# 			messages.success(request, "グレースケールに変換しました！")
	# 		elif obj.description == "モザイク":
	# 			small = cv2.resize(img, None, fx=0.1, fy=0.1, interpolation=cv2.INTER_NEAREST)
	# 			big = cv2.resize(small, img.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)
	# 			cv2.imwrite(output_path, big)
	# 			output_path = output_path.replace("/Users/suehiro/1pro/Django/image_app/ImageService/media", "")
	# 			photo_data.output = output_path
	# 			photo_data.save()
	# 			messages.success(request, "モザイクをかけました！")
	# 		elif obj.description == "フェイスモザイク":
	# 			face_cascade_path = settings.BASE_DIR + "/data/haarcascade_frontalface_default.xml"
	# 			face_cascade = cv2.CascadeClassifier(face_cascade_path) # カスケード分類器のファイルの中身を読み込む
	# 			src_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #RGBからグレースケールに変換
	# 			rects = face_cascade.detectMultiScale(src_gray, 1.1, 3,0, (20,20))
	# 			if len(rects) > 0:
	# 				for rect in rects:
	# 					x, y, w, h = rect
	# 					face = img[y:y+h, x:x+w]
	# 					dst = cv2.GaussianBlur(face, (25, 25), 0)
	# 					img[y:y+h, x:x+w] = dst
	# 			else:
	# 				pass
	# 			cv2.imwrite(output_path, img)
	# 			output_path = output_path.replace("/Users/suehiro/1pro/Django/image_app/ImageService/media", "")
	# 			photo_data.output = output_path
	# 			photo_data.save()
	# 			messages.success(request, "顔にモザイクをかけました！")
	# 		elif obj.description == "モザイクgif":
	# 			src= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	# 			imgs = [Image.fromarray(mosaic(src, 1 / i)) for i in range(1, 25)]
	# 			imgs += imgs[-2::-1] + [Image.fromarray(src)] * 5
	# 			imgs[0].save(output_path_gif, commit=False, save_all=True, append_images=imgs[1:], optimize=False, duration=50, loop=0)
	# 			output_path_gif = output_path_gif.replace("/Users/suehiro/1pro/Django/image_app/ImageService/media", "")
	# 			photo_data.output = output_path_gif
	# 			photo_data.save()
	# 			messages.success(request, "モザイクgifに変換しました！") 
	# 		else:
	# 			pass

	# 		return redirect('image_app:index')

	# else:
	# 	form = DocumentForm()

	# return render(request, 'image_app/index.html', {'form': form, 'document_list': document_list, })

@login_required
def users_detail(request, pk):
	login_user = request.user.pk
	user = get_object_or_404(User, pk=pk)
	print(user)
	document_list = user.document_set.all().order_by('-id')
	print(document_list)

	if request.method == 'POST':
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			photo_data = form.save(commit=False)
			photo_data.user = request.user
			photo_data = form.save()
			max_id = Document.objects.latest('id').id
			max_id_str = str(max_id)
			obj = Document.objects.get(id = max_id)
			input_path = settings.BASE_DIR + obj.photo.url
			output_path = settings.BASE_DIR + "/media/output/" + max_id_str + ".jpg"
			output_path_gif = settings.BASE_DIR + "/media/output/" + max_id_str + ".gif"
			img = cv2.imread(input_path)
			if obj.description == "グレースケール":
				img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
				cv2.imwrite(output_path, img_gray)
				output_path = output_path.replace("/Users/suehiro/1pro/Django/image_app/ImageService/media", "")
				photo_data.output = output_path
				photo_data.save()
				messages.success(request, "グレースケールに変換しました！")
			elif obj.description == "モザイク":
				small = cv2.resize(img, None, fx=0.1, fy=0.1, interpolation=cv2.INTER_NEAREST)
				big = cv2.resize(small, img.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)
				cv2.imwrite(output_path, big)
				output_path = output_path.replace("/Users/suehiro/1pro/Django/image_app/ImageService/media", "")
				photo_data.output = output_path
				photo_data.save()
				messages.success(request, "モザイクをかけました！")
			elif obj.description == "フェイスモザイク":
				face_cascade_path = settings.BASE_DIR + "/data/haarcascade_frontalface_default.xml"
				face_cascade = cv2.CascadeClassifier(face_cascade_path) # カスケード分類器のファイルの中身を読み込む
				src_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #RGBからグレースケールに変換
				rects = face_cascade.detectMultiScale(src_gray, 1.1, 3,0, (20,20))
				if len(rects) > 0:
					for rect in rects:
						x, y, w, h = rect
						face = img[y:y+h, x:x+w]
						dst = cv2.GaussianBlur(face, (25, 25), 0)
						img[y:y+h, x:x+w] = dst
				else:
					pass
				cv2.imwrite(output_path, img)
				output_path = output_path.replace("/Users/suehiro/1pro/Django/image_app/ImageService/media", "")
				photo_data.output = output_path
				photo_data.save()
				messages.success(request, "顔にモザイクをかけました！")
			elif obj.description == "モザイクgif":
				src= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
				imgs = [Image.fromarray(mosaic(src, 1 / i)) for i in range(1, 25)]
				imgs += imgs[-2::-1] + [Image.fromarray(src)] * 5
				imgs[0].save(output_path_gif, commit=False, save_all=True, append_images=imgs[1:], optimize=False, duration=50, loop=0)
				output_path_gif = output_path_gif.replace("/Users/suehiro/1pro/Django/image_app/ImageService/media", "")
				photo_data.output = output_path_gif
				photo_data.save()
				messages.success(request, "モザイクgifに変換しました！") 
			else:
				pass

			return redirect('image_app:users_detail', pk=request.user.pk)

	else:
		form = DocumentForm()

	return render(request, 'image_app/users_detail.html', {'form': form, 'document_list': document_list, 'user': user})

def mosaic(src, ratio=0.1):
    small = cv2.resize(src, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
    return cv2.resize(small, src.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)


@require_POST
def delete(request, pk):
	delete_data = get_object_or_404(Document, pk=pk)
	delete_data.delete()
	messages.success(request, "データを削除")
	return redirect('image_app:users_detail', request.user.id)

def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			input_username =form.cleaned_data['username']
			input_password = form.cleaned_data['password1']
			#usernameとpasswordを引数に取り、その組み合わせで認証に成功すればUserオブジェクトを返す。認証できなければNoneを返す。
			new_user = authenticate(username=input_username, password=input_password)
			if new_user is not None:
				# リクエスト情報とUserオブジェクトを引数に取り、そのユーザーを未ログイン状態からログイン状態にする。
				# login(request, new_user)
				# return redirect('image_app:login', pk=new_user.pk)
				messages.success(request, "ユーザー登録が完了しました！") 
				return redirect('image_app:login')
	else:
		form = UserCreationForm()
	return render(request, 'image_app/signup.html', {'form': form})






