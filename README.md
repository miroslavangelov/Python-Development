# Workshop: Petstagram - 1
Throughout the whole module we are going to be creating a complete Django project called "Petstagram". The project will cover the following functionalities: registration/login, user profile (with profile picture that can be changed); a user will be able to view all photos of pets, open details, comment and like a photo, edit and delete their own pet photos. 
##    1. Final Project
Home Page
![petstagram1](https://user-images.githubusercontent.com/67734870/120034619-fb64f880-c005-11eb-9af2-3afa1d133a1d.png)
Register

![petstagram1](https://user-images.githubusercontent.com/67734870/120034754-31a27800-c006-11eb-98e6-905867be6b02.png)

Login
![petstagram1](https://user-images.githubusercontent.com/67734870/120034830-4e3eb000-c006-11eb-8a48-7811b8a1f831.png)
Create
![petstagram1](https://user-images.githubusercontent.com/67734870/120034904-6adae800-c006-11eb-8bb3-d8a5a60bd7c5.png)
All Pet Photos
![petstagram1](https://user-images.githubusercontent.com/67734870/120034985-8940e380-c006-11eb-9d2c-d137c287ed04.png)
Pet Details (not own)
![petstagram1](https://user-images.githubusercontent.com/67734870/120035058-a70e4880-c006-11eb-9f0a-b0693f93c773.png)
Pet Details (own)
![petstagram1](https://user-images.githubusercontent.com/67734870/120035196-dd4bc800-c006-11eb-82f5-2189379e6bea.png)
Pet Edit
![petstagram1](https://user-images.githubusercontent.com/67734870/120035258-f3598880-c006-11eb-9a29-e033e06cd835.png)
Pet Delete
![petstagram1](https://user-images.githubusercontent.com/67734870/120035311-0d936680-c007-11eb-9db7-35ad81f8dc1b.png)
Profile
![petstagram1](https://user-images.githubusercontent.com/67734870/120035351-213ecd00-c007-11eb-998f-1c2186b0b9a9.png)
##    2. Part I – The Landing Page
Setup
Let us start by creating the project
![petstagram1](https://user-images.githubusercontent.com/67734870/120035422-43384f80-c007-11eb-8e67-8d99e397ab9a.png)
Now, let us create the first app which will be called 'common' which will contain all the common parts of our project, including the language page
![petstagram1](https://user-images.githubusercontent.com/67734870/120035489-5e0ac400-c007-11eb-97b8-226feecc28df.png)
The next step will be to create the templates folder

![petstagram1](https://user-images.githubusercontent.com/67734870/120035552-7a0e6580-c007-11eb-887b-f90cfea1ea5c.png)
### Configurations
Now, we need to do some configurations. We will start with configuring our templates path
![petstagram1](https://user-images.githubusercontent.com/67734870/120035639-98746100-c007-11eb-80f7-f1b9a7ed6727.png)
![petstagram1](https://user-images.githubusercontent.com/67734870/120035746-bb067a00-c007-11eb-94cd-75ce37fbd100.png)
Then, we need to add the app we just created in the INSTALLED_APPS

![petstagram1](https://user-images.githubusercontent.com/67734870/120035852-ebe6af00-c007-11eb-8d2d-c511bbbb1581.png)

### Migrations and Starting the Project
![petstagram1](https://user-images.githubusercontent.com/67734870/120035969-146ea900-c008-11eb-95c6-a32c8058ed41.png)
![petstagram1](https://user-images.githubusercontent.com/67734870/120036025-2cdec380-c008-11eb-841f-401a74a26d5a.png)
![petstagram1](https://user-images.githubusercontent.com/67734870/120036087-45e77480-c008-11eb-9f2e-7c5e123f6eea.png)
### Creating the Landing Page
Let us first create the html file of the landing page and write the html in it

![petstagram1](https://user-images.githubusercontent.com/67734870/120036178-66173380-c008-11eb-8130-764f7f0aa59e.png)

Copy the content of the given html file and paste it in your html file
Now, we can create the view

![petstagram1](https://user-images.githubusercontent.com/67734870/120036233-79c29a00-c008-11eb-911a-f96517305b00.png)

Now, create the urls.py file and write the following code

![petstagram1](https://user-images.githubusercontent.com/67734870/120036275-9068f100-c008-11eb-9a58-68b682fb115d.png)

Finally, we need to include the urls from the app in our project

![petstagram1](https://user-images.githubusercontent.com/67734870/120036317-a4acee00-c008-11eb-961c-5a9e793c256e.png)

Now we can start the project

![petstagram1](https://user-images.githubusercontent.com/67734870/120036376-b9898180-c008-11eb-83fe-42186d5e434e.png)

# Workshop: Petstagram - 2
 ##   1. Part II – The Pet Models and Views
Creating the 'pets' app
For our pet logic we will have a separate app, so let us create it first

Add the new app in the INSTALLED_APPS in the settings.py file of the project
## Creating the Models
### In the models.py file create the Pet model. Each pet should have:
    • type – some of the following: "cat", "dog", "parrot"; max length = 6
    • name – max length = 6
    • age – positive number
    • description – text field
    • image_url – URL field
### Now in the models.py file create Like model. Each like should have:
    • pet – foreign key to a Pet
Let us also register our models in the admin.py file in the app, so we can see it in the django admin
## Make Migrations
The next step is to make migrations to the database, since we created some new models
Let us also create a superuser, so we can create some pets using the django admin
## Create Pets
Create some pets, so we can test our views that we will create later

![1](https://user-images.githubusercontent.com/67734870/121063918-9791bb00-c7cf-11eb-96b6-5a265c7dd020.png)

## Creating Some Views
### Let us now start creating some of our views. We will create the pet_all view and the pet_detail view
    • 'localhost:8000/pets/' - list all the pets (using the pet_all view and a template 'pets/pet_list.html')
    • 'localhost:8000/pets/details/<int:pk>' - display the pet with the given primary key (using the pet_detail view and a template 'pets/pet_detail.html')
    • 'localhost:8000/pets/like/<int:pk>' - write a view that will create a new like and redirect the user to the details page again
Use the provided html files and add the needed logic in them, so they work as expected
![1](https://user-images.githubusercontent.com/67734870/121064136-dcb5ed00-c7cf-11eb-8712-70838ba2bd77.png)
![1](https://user-images.githubusercontent.com/67734870/121064201-f0615380-c7cf-11eb-9b80-f4fc1827ba3c.png)
## Add Additional Links
In the navigation edit the 'Home' link to lead to the landing page and add another link that leads to 'pet-list'
![1](https://user-images.githubusercontent.com/67734870/121064284-08d16e00-c7d0-11eb-8024-78ae46ddf4f3.png)
![1](https://user-images.githubusercontent.com/67734870/121064330-1850b700-c7d0-11eb-91a4-00e0ab8ea11d.png)

# Workshop: Petstagram
##    1. Part III – The Pet Forms and Comments
### Creating the Comment model
#### In the "common" app create a model called Comment with the following fields:
    • pet – foreign key
    • comment – text field
### Creating forms
#### In the "pets" app create a file called forms.py and create a PetCreateForm:
```
class CreatePetForm(forms.ModelForm):
    type = forms.ChoiceField(choices=[("dog", "dog"), ("cat", "cat"), ("parrot", "parrot")], required=True, widget=forms.Select(
        attrs={
            'class': 'form-control'
        },
        
    ))
    name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    age = forms.IntegerField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'type': 'number'
        }
    ))
    image_url = forms.URLField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    description = forms.CharField(required=True, widget=forms.Textarea(attrs={
        'class': 'form-control rounded-2'
    }))

    class Meta:
        model = Pet        
        fields = ('type', 'name', 'age', 'description', 'image_url')
```
#### and in the "common" app create a file called forms.py with the CommentForm:
```
class CommentForm(forms.Form):
    comment = forms.CharField(required=True, widget=forms.Textarea(attrs={
        'class': 'form-control rounded-2'
    }))

    class Meta:
        model = Comment
        fields = ('comment')
```
## New URL's
### Create the following new urls and implement the needed views in the 'pets' app:
    • GET 'localhost:8000/pets/create' – open a form for pet creation
    • POST 'localhost:8000/pets/create' – validate the form, create the new pet and redirect the user to the 'all pets' page
    • GET 'localhost:8000/pets/edit/<int:pk>' – open an edit form for a pet
    • POST 'localhost:8000/pets/edit/<int:pk>' – validate the form, edit the pet info and redirect the user to the 'pet detail' view of the current pet
    • GET 'localhost:8000/pets/delete/<int:pk>' – render the given 'pet-delete.html'
    • POST 'localhost:8000/pets/delete/<int:pk>' – delete the pet and redirect the user to the 'all pets' page
    • POST 'localhost:8000/pets/detail/<int:pk>' – get the information of the comment form, create new comment and redirect the user to the details page again
## Templates
For the new views you are provided with the needed 'html' files. Beware that the logic in them is NOT implemented. You need to implement it on your own.
### Additions to old templates
pet-detail.html
### Adding the 'Edit' and 'Delete' buttons
```
<a href="url to the edit view" class="btn btn-success">Edit</a>
<a href="url to the delete view" class="btn btn-danger">Delete</a>
```
### Adding the comment div
```
<div class="d-block" style="background-color: #f1e3e3; padding:2%">
    if comments
    for each comment
    <div class="box">
        <h5><em>comment_content</em></h5>
        <hr>
    </div>
    else
    <div class="box">
        <h3>There are no comments for this pet. </h3>
    </div>
    endif
    <div class="box">
        <form method="post">
            comment_form
            <button class="btn btn-primary mt-2" type="submit">Add comment</button>
        </form>
    </div>
</div>
```
## Results
localhost:8000/pets/createlocalhost:8000/pets/details/<int:pk>

![1](https://user-images.githubusercontent.com/67734870/122684681-82754d00-d20f-11eb-893d-0a17abaa8412.png)

localhost:8000/pets/details/<int:pk>

![1](https://user-images.githubusercontent.com/67734870/122684695-9b7dfe00-d20f-11eb-8a99-8105e56eb564.png)

localhost:8000/pets/edit/<int:pk>

![1](https://user-images.githubusercontent.com/67734870/122684766-265ef880-d210-11eb-9aba-32434f9a9966.png)

localhost:8000/pets/delete/<int:pk>

![1](https://user-images.githubusercontent.com/67734870/122684781-41ca0380-d210-11eb-8b5f-f9745c6e3f54.png)


# Workshop: Petstagram
##    1. Part IV – Template Inheritance and Media Files
### Modifying the Pet Model
Modify the Pet model, so the image field is not a URL, but a file and make migrations to the database
### Modifying the Forms
Modify the form of the pet, so the field is a file field
### Modifying the Views
Modify the edit and create views, so they save the pet photos in the media folder
### Modifying the Templates
Separate the main parts of your templates, so you use template inheritance and make the changes needed to display the images correctly
### Results

![1](https://user-images.githubusercontent.com/67734870/124760163-20b82100-df39-11eb-9612-16dcea6aa5c4.png)

![1](https://user-images.githubusercontent.com/67734870/124760229-33325a80-df39-11eb-99df-c0e102a09cd7.png)

![1](https://user-images.githubusercontent.com/67734870/124760295-4513fd80-df39-11eb-8e48-b2eaf19bf44f.png)

![1](https://user-images.githubusercontent.com/67734870/124760360-578e3700-df39-11eb-9ee5-99d5c31b8d3b.png)


# Workshop: Petstagram
##    1. Part V – Users
Creating 'accounts' app
Create a new app called 'accounts', where the registration, login, logout and user profiles will be handled
### UserProfile model
### In the new app create an UserProfile model with the following fields:
    • user – foreign key to the user
    • profile_picture – picture upload
### New url's
### Add the following urls:
    • GET 'localhost:8000/accounts/' – include the django.contrib.auth.urls
    • GET 'localhost:8000/accounts/profile/<int:pk>' – create a view that will render the provided 'user_profile.html' with the needed information
    • POST 'localhost:8000/accounts/profile/<int:pk>' – update the profile picture of the user
    • GET 'localhost:8000/accounts/signup' – render the provided 'signup.html' with the register form
    • POST 'localhost:8000/accounts/signup' – register the user and create a user profile (with the default.png as profile picture)
### Modifying old models
    • Pet model – add a new field called user which is linked to an UserProfile
    • Comment model – add a new field called user which is linked to an UserProfile
    • Like model - add a new field called user which is linked to an UserProfile
### Modifying old templates
    • Add login/logout/register links in the navbar and implement the needed template logic
    • In the pet_detail template, implement the logic, so the edit and delete buttons are visible only in the pet belongs to the user. If not, display the 'heart' button (filled if the user has liked the pet already, not filled if the user has not yet liked this pet). Display the comment form if the pet does not belong to the user.
### Restrictions
Only logged in users can view and create pet photos.
### Results
Current user is not an owner and has not yet liked this photo. The user can also comment the photo

![1](https://user-images.githubusercontent.com/67734870/126627879-45fef289-38c6-4403-bd42-7d62084f2c5a.png)

After the user has liked the photo:

![1](https://user-images.githubusercontent.com/67734870/126627942-98fda765-ec26-4297-a8e3-fd693347292e.png)

The owner cannot like his photo and cannot post comments. He can edit/delete his pet photo

![1](https://user-images.githubusercontent.com/67734870/126628001-6c9d8d5d-82e9-429f-9111-2a9e704b7d42.png)

User profile

![1](https://user-images.githubusercontent.com/67734870/126628062-51a8eb3a-f27c-4d51-9746-af702e7e2462.png)



