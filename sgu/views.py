from django.shortcuts import render, redirect
#from .forms import TeacherSignUpForm, ParentSignUpForm

# def teacher_signup(request):
#     if request.method == 'POST':
#         form = TeacherSignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')  # Replace 'home' with the URL you want to redirect after successful signup
#     else:
#         form = TeacherSignUpForm()
#     return render(request, 'signup.html', {'form': form})

# def parent_signup(request):
#     if request.method == 'POST':
#         form = ParentSignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')  # Replace 'home' with the URL you want to redirect after successful signup
#     else:
#         form = ParentSignUpForm()
#     return render(request, 'signup.html', {'form': form})
