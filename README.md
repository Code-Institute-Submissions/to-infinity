![Mockup on all Devices](https://res.cloudinary.com/fdeboo/image/upload/v1611907032/toinfinity_readme/multidevicemockup_chz16s.png)

# Table of contents

1. [Introduction](#introduction)
    * [Objective](#objective)
    * [User stories](#users)
    * [Design Notes](#design)
    * [Wireframes](#wireframes)
2. [UX](#design)
3. [Features](#features)
    * [Existing Features](#existing_feat)
    * [Features left to implement](#future_feat)
4. [Information Architecture](#models)
5. [Technologies Used](#technologies)
6. [Testing](#testing)
7. [Deployment](#deploying)
    * [Run Locally](#local)
    * [Deploy to Heroku](#heroku)
8. [Credits](#credits)
    * [Content](#content)
    * [Media](#media)
    * [Acknowledgements](#acknowledgements)

# Introduction <a name="introduction"></a>

## Objective <a name="strategy"></a>

* To sell trips to outer space

## User Stories <a name="users"></a>

"As a user, I would like to \_\_\_\_\_\_\_\_\_\_\_"

* As a user, I would like to view the different types of trips available
* As a user, I would like to view individual trips in more detail
* As a user, I would like to book my place on a trip
* As a user, I would like to provide details of the number of passengers and passenger information
* As a user, I would like to review my booking before placing it
* As a user, I would like to easily Enter Payment information
* As a user, I would like to feel my personal and payment information is secure
* As a user, I would like to view my order confirmation after checkout
* As a user, I would like to receive a confirmation email after the checokout is complete
* As a user, I would like to modifiy my booking details
* As a user, I would like to view my bookings

"As a business user, I would like to"

* As a buisness owner I would like to add new trips and experiences
* As a buisness owner I would like to view the number of seats available for each trip


## Design Notes <a name="design"></a>

### Fonts
The fonts for this project were sourced from [Google Fonts](https://fonts.google.com/)

+ **"Montserrat"** is the main font used for the body text, links, buttons and subheadings. It was chosen because of it's easy legibility and low contrast strokes that give it a clean, modern feel. The font comes in a good range weights which make it flexible for emphasising words in bold or adding subtle hover effect to links. Montserrat pairs well with the secondary font because of it's smooth, circular curves that contrast with the square form of Orbitron's letters,

+ The secondary font used for this app is **"Orbiton"**, a sans serif font reminiscent of futuristic sci-fi movies. The geometric typeface was designed for display purposes and as such, is used for 2infinity's main logo and headings. It was chosen for it's strong futuristic character which supports the theme of the app.

+ The font used for the hero text on the landing page is **"Euphoria Script"**. It was chosen to contrast the main display font (Orbitron) for added interest. It is set to a large font size for maximum impact and legibility and given a text shadow which matches the base teal colour chosen for the site.

### Icons

+ Icons are used as visual cues against each of the navigation links in the header.
+ Social Media Icons are included in the footer in lieu of written links as the icons are more immediately recognizable.
+ On the user profile page, the table headings are shortened by using icons to save space.
+ Used in the porgress bar

### Colours
[Adobe Color](https://color.adobe.com/create) was used to develop the colours for 2infinty.

The brand has a dark theme to reflect the darkness of outer space. Cyan, used for the base colour, is a bright, additative secondary colour created by mixing blue and green light. It was chosen because it captures the glow of Earth as viewed from space.


#### Base 
**#2AB1B7**: Used for h1 Headings, borders, underlines, the hero button and the footer
 
#### Split Complementary
 **#B88421**: Warnings & form errors

![Split Complementary Colours](https://res.cloudinary.com/fdeboo/image/upload/v1611907001/toinfinity_readme/splitcomplementary_a1zubd.png "Split Complementary Colours")

#### Complementary
**#0E666B**: Text in the page footer. The contrast from the base cyan is enough to be legible without grabbing too much attention

![Complementary Colours](https://res.cloudinary.com/fdeboo/image/upload/v1611907001/toinfinity_readme/splitcomplementary_a1zubd.png "Complementary Colours")

#### Monochromatic
**#0D3638**: Bottom border colour for form inputs

![Monochromatic Colours](https://res.cloudinary.com/fdeboo/image/upload/v1611906927/toinfinity_readme/monochromatic_lokvxw.png "Monochromatic Colours")

#### Square
**#99B821**: For links, highlighting selected options and progress bar icons.

![Square Colours](https://res.cloudinary.com/fdeboo/image/upload/v1611907007/toinfinity_readme/square_ucnx3j.png "Square Colours")


## Wireframes <a name="wireframes"></a>

The [Bootstrap](https://getbootstrap.com/) framework was used extensively throughout the app to acheive responsive layouts.

### Base Skeleton  

+ The pager header, containing the navigation links and company logo, is anchored to the top of the viewport window and has a high z-index so that the page content scrolls behind it.

+ When the entire body fits within the viewport height, the footer anchors to bottom of the screen while the main content 'grows' to fill the remaining space.

+ If the main content overflows the viewport height, the content becomes scrollable and the footer is positioned as per default, in the normal flow of the page.  

+ The content is structured using Bootstrap's Grid System. On all screen sizes, the containing elements - **header**, **main**, and **footer** are given the class **"container-fluid"** so that the background extends accross the full width of the screen.

+ The content within the **header** and **main** elements is contained within a content column. This is a full width column (**"col-12"**) on small devices, but reduced to 83.33\% width on viewports wider than 991px, to allow a margin on the left and right of content (**"col-md-10"**)

+ On all devices, the content column within the footer is set to (**"col-12"**) which gives the page a solid base.

&nbsp;
![Base Template](https://res.cloudinary.com/fdeboo/image/upload/v1611906919/toinfinity_readme/base_layout_oevyil.png "Base Structure")

&nbsp;
### Home 
&nbsp;
![Landing Page](https://res.cloudinary.com/fdeboo/image/upload/v1611914508/toinfinity_readme/home_krv0lm.png "Landing Page Template")


&nbsp;
### AllAuth Templates 

+ The templates to sign in, sign up and sign out all conform to the base structure of the app; The header is anchored at the top and the main content is centered vertically and horizontally, filling the space between the header and the footer at the bottom of the screen.

+ The individual forms are the only features of their respective templates and are styled as per the form style.

+ On larger screen sizes the forms are contained by a 1px solid border in the base teal colour. On mobile devices, the border is removed as viewport comfortably takes over as the form's 'container'.

&nbsp;
#### Sign Up   
&nbsp;
![All auth Sign Up](https://res.cloudinary.com/fdeboo/image/upload/v1611914519/toinfinity_readme/register_kql8mx.png "Sign Up Template")

&nbsp;
#### Sign In
&nbsp;
![All auth Sign In](https://res.cloudinary.com/fdeboo/image/upload/v1611914511/toinfinity_readme/signin_uclenn.png "Sign In Template Page")

&nbsp;
#### Sign Out
&nbsp;
![All auth Sign Out](https://res.cloudinary.com/fdeboo/image/upload/v1611914502/toinfinity_readme/signout_lkkeqi.png"Sign Out Template Page")


&nbsp;
### View Trips
&nbsp;
![Destination List](https://res.cloudinary.com/fdeboo/image/upload/v1611914500/toinfinity_readme/viewtrips_vpfecc.png "Destination List template Template")

&nbsp;
### Destination Detail
&nbsp;
![Destination Detail]( "Destination Detail")

&nbsp;
### Book A Trip
&nbsp;
![Book a Trip](https://res.cloudinary.com/fdeboo/image/upload/v1611914525/toinfinity_readme/searchtrips_g02zti.png "Search Trip Template")

&nbsp;
### Confirm Trip
&nbsp;
![Confirm Trip](https://res.cloudinary.com/fdeboo/image/upload/v1611914507/toinfinity_readme/confirmtrips_pt2lll.png "Confrim Trip Template")

&nbsp;
### Passenger Details
&nbsp;
![Passenger Details](https://res.cloudinary.com/fdeboo/image/upload/v1611914507/toinfinity_readme/confirmtrips_pt2lll.png "Passenger Details Template")

&nbsp;
### Checkout
&nbsp;
![Checkout](https://res.cloudinary.com/fdeboo/image/upload/v1611914509/toinfinity_readme/checkout_xna2g2.png "Checkout Template")

&nbsp;
### Checkout Success
&nbsp;
![Checkout Success](https://res.cloudinary.com/fdeboo/image/upload/v1611914508/toinfinity_readme/checkoutsuccess_p4hcr9.png "Checkout Success Template")

&nbsp;
### User Profile
&nbsp;
![User Profile](https://res.cloudinary.com/fdeboo/image/upload/v1611914507/toinfinity_readme/userprofile_yqkofy.png "User Profile Template")


# Features <a name="features"></a>
## Existing Features <a name="existing"></a>

### Home App
+ The layout of the landing page is minimalistic and draws the user directly to the hero button which offers a starting point for their navigation of the site.

+ The page is filled with a dynamic full screen background image of the Earth
photographed from space. The image is fixed so that image appears to zoom in and out when the viewport is resized but keeps its position on the page. 

+ The base teal colour is used to catch the eye as it stands out againt the dark theme. In this template, it is used in the header section to underline the hovered navigation links, in the main section for the hero button and effect on the hero text, and for footer. This keeps the overall template nicely balanced.

&nbsp;
### Booking App    
&nbsp;

#### Progress Bar
&nbsp;
![Progress Bar](https://res.cloudinary.com/fdeboo/image/upload/v1611906942/toinfinity_readme/progressbar_fq5nmi.png "Progress Bar")
+ The templates in the booking process feature a progress bar just beneath the main navigation bar. This is positioned 'sticky' so that it retains it's position if the page requires scrolling.

* The progess bar enables the user to track where they are in the booking process.

+ The active step, and any steps that preceed it in the booking processs are highlighted and their links are enabled. The steps beyond the active step are greyed out and links are disabled. 

+ On smaller screen sizes, the size of the progress bar icons reduces slightly to keep in keep in proportion with the space.

+ The first step in the progress bar is an active link back to the Search Trips template.

&nbsp;
#### Search Trips Form
&nbsp;
![Search Trips](https://res.cloudinary.com/fdeboo/image/upload/v1611907015/toinfinity_readme/searchtripsform_omwcg3.png "Search Trips")
+ The form appears in the 'Search Trips' template but is also featured on the 'View Trips' page



+ The Passengers field is disabled until a Destination is selected from the dropdown list.
This is so that the **max** attribute for the passengers input is dynamically set using jquery when it detects a change in the Destination field.    


```
$('#selected-trip').change(function() {
    if ($('#selected-trip').val() == '') {
        $('#passengers-max').prop("disabled", true);
    }
    else {
        let maxNm = $('#selected-trip option:selected').data('maxNum');         
        $('#passengers-max').attr("max", maxNm).prop("disabled", false);
    }
});
```

+ For this to work, I created a custom widget, sublassing Django's Select widget and customising its 'create_option' method.  The customised method allows the **max\_passengers** value for the represented destination instance, to be be passed as a data attribute to the option element.

```
def create_option(
        self, name, value, label, selected, index, subindex=None, attrs=None
    ):
        if isinstance(label, dict):
            opt_attrs = label.copy()
            label = opt_attrs.pop("label")
        else:
            opt_attrs = {}
        option_dict = super(SelectOptionsWithAttributes, self).create_option(
            name, value, label, selected, index, subindex=subindex, attrs=attrs
        )
        for key, val in opt_attrs.items():
            option_dict["attrs"][key] = val
        return option_dict
```

&nbsp;
#### Confirm Trips Form

+ The form contains a set of radio input options based on a filtered queryset. The Trips are initially filtered by destination and then by seats available. The set of options is further refined to the dates closest to the date that the user requested.  

+ The radio buttons are hidden in favor of custom styled input labels which display the date, and price per person.


![Customised Radio Inputs](https://res.cloudinary.com/fdeboo/image/upload/v1611906970/toinfinity_readme/customradiobtn_iys5yk.png "Custom Radio Inputs")


+ When the option is submitted, a model is triggered to confirm that the choices that the passenger has made.

&nbsp;
#### Passenger Formset

+ The Formset receives a value for the number of passengers given in the booking and uses it to define the number of forms in the formset.

+ The Addons for the trip are represented as a set of checkboxes but the checkboxes are customised to base on a 
![Custom Checkboxes](https://res.cloudinary.com/fdeboo/image/upload/v1611906970/toinfinity_readme/customradiobtn_iys5yk.png "Confirm Model")



#### Booking Summary

## Future Features

+ Asynchronous Housekeeping  
This enhancement would aim to implement structures that make it easy introduce asynchronous housekeeping as requirements are identified, the first example being removal from the database of expired open bookings--bookings created and saved, perhaps by one-time visitors to the site, but never completed.  Any open bookings against expired trips would be targets for this housekeeping.  There are two parts to the implementation of each asynchronous housekeeping requirement:

    + A Python script that executes the specific housekeeping; in the case of expired open bookings, the sole objective of the script is to issue an database query along the lines of "BEGIN; DELETE BOOKING WHERE BOOKING.STATUS = 'Open' AND BOOKING.TRIP = TRIP.PK AND TRIP.DATE < CURRENT_DATE; END"
    A means to schedule the periodic execution of the script which, in the case of open bookings, is the frequency with which open bookings may become expired.  This would be explored using some combination of Django async views, the Django-Q addon, and Heroku Redis as a queue dispatching service. 

    + Thereafter, each additional housekeeping requirement would be implemented by creating the appropriate housekeeping script, and the additional statements within the async view to invoke the script on the appropriate scheduling basis.

+ Passenger Medical Assessments    
At the moment, 2Infinity bookings accept any Passengers named by the user.  But flights to deep space, or addons such as space walks or space buggy rides, may not be suitable for certain Passengers based on age (too young or too old) or certain medical or physical conditions.  The enhancement would introduce a model whereby each Passenger could be issued with a medical assessment questionnaire, the completion of which becomes a condition for accepting the Passenger for the Trip.  Theoretically, the 2Infinity shop could communicate with a nominated GP for each Passenger to receive the GP's verdict on the Passenger's suitability for the Trip Booking and addon activities.


# Information Architecture <a name="models"></a>

## Models

- - -

## Profile

### UserProfile:

| Name | Key in db | Field Type | Options |
| ---- | --------- | ---------- | ------- |
| User | user | OneToOneField(User) | on\_delete=CASCADE |
| First Name | default\_first\_name | CharField | max\_lenghth=80, null=False, blank=False |
| Last Name | default\_last\_name | CharField | max\_length=80, null=False, blank=False |
| Phone Number | default\_phone\_num | CharField | max\_length=20, null=True, blank=True |
| Passport Number | default\_passport\_num | CharField | max\_length=9, min\_length=9,null=False, blank=False |
| Medical Rating | default\_medical\_rating | IntegerField | null=true, blank=True |

- - -

Booking

&nbsp;
### Trip:

| Name | Key in db | Field Type | Validation |
| ---- | --------- | ---------- | ---------- |
| Destination | destination | ForeignKey(Destination) | null=True, blank=False, on\_delete=SET\_NULL |
| Date | date | DateField |  |
| Seats Available | seats\_available | IntergerField | null=False, blank=False, editable=False |

### Booking:

| Name | Key in db | Field Type | Validation |
| ---- | --------- | ---------- | ---------- |
| Booking Reference | booking\_ref | CharField | primary\_key=True, max\_length=20, null=False, editable=False |
| Trip | trip | ForeignKey(Trip) | on\_delete=SET\_NULL, null=False, blank=False |
| Lead User | lead\_user | ForeignKey(UserProfile) | on\_delete=SET\_NULL, null=True, blank=True |
| Booking Total | booking\_total | DecimalField | max\_digits=10, decimal\_places=2, null=False, default=0 |
| Stripe Payment ID | stripe\_pid | CharField | max\_length=254, null=False, blank=False default="" |
| Full Name | full\_name | TextField | max\_length=50, null=False, blank=False |

### Passengers:

| Name | Key in db | Field Type | Validation |
| ---- | --------- | ---------- | ---------- |
| Booking | booking | ForeignKey(Booking) | on\_delete=CASCADE, |
| First Name | first\_name | CharField | on\_delete=SET\_NULL, null=False, blank=False |
| Last Name | last\_name | CharField | on\_delete=SET\_NULL, null=True, blank=True |
| Email | email | EmailField | max\_length=254, null=False, blank=False |
| Passport Number | passport_no | CharField | max\_length=9, min\_length=9, null=False, blank=False |
| Lead Passenger | is_leadpassenger | BooleanField | null=False, blank=False |
| Trip Addons | trip_addons | ManyToMany(Addon) | null=True, blank=True |
| Trip Insurance | trip_insurance | ForeignKEy(Insurance) | on\_delete=SET\_NULL |
| Medical Assessment | medical\_assessment | OneToOneField(Medical) | on\_delete\_CASCADE, null=True, blank=True |
| Medical Rating | medical\_rating | IntegerField | max\_digits=3, null=False, blank=False, default=0 |

### Booking Line Items:

| Name | Key in db | Field Type | Validation |
| ---- | --------- | ---------- | ---------- |
| Booking | booking | ForeignKey(Booking) | on\_delete=SET\_NULL, null=False, blank=False, on\_delete=CASCADE |
| Product | product | OneToOneField(Product) | on\_delete=SET\_NULL, null=False, blank=False, on\_delete=CASCADE |
| Quantity | quantity | IntegerField | null=False, blank=False, default=0 |
| Line Total | line\_total | DecimalField | max\_digits=7, decimal\_places=2, null=False, blank=False, editable=False |

- - -

## Products

### Product:

| Name | Key in db | Field Type | Validation |
| ---- | --------- | ---------- | ---------- |
| Category | category | ForeignKey(Category) | null=True, blank=True, on\_delete=SET\_NULL |
| Name | name | CharField | max\_length=254 |
| Product ID | product\_id | CharField | max\_length=254 |
| Description | description | TextField |  |
| Price | price | DecimalField | max\_digits=6, decimal\_places=2 |
| Image | image | ImageField | null=True, blank=True |
| Image URL | image\_url | URLField | max\_length=1024, null=True, blank=True |
| Image Thumbnail | image\_thumb | ImageField | null=True, blank=True |

### Category:

| Name | Key in db | Field Type | Validation |
| ---- | --------- | ---------- | ---------- |
| Name | name | CharField | max\_length=75 |
| Friendly Name | friendly\_name | CharField | max\_length=75, blank=True |

### Destination (Product):

| Name | Key in db | Field Type | Validation |
| ---- | --------- | ---------- | ---------- |
| Maximum Passengers | max\_passengers | IntegerField |  |
| Duration | duration | CharField | max\_lenght=20 |
| Minimal Medical Threshold | min\_medical\_threshold | IntegerField | blank=True |

### Add-On (Product):

| Name | Key in db | Field Type | Validation |
| ---- | --------- | ---------- | ---------- |
| Minimal Medical Threshold | min\_medical\_threshold | IntegerField |  |

### Insurance (Product):

| Name | Key in db | Field Type | Validation |
| ---- | --------- | ---------- | ---------- |
| Friendly Name | friendly\_name | CharField | max\_length=75, blank=True |

- - -

![Schema](https://res.cloudinary.com/fdeboo/image/upload/v1611906975/toinfinity_readme/schema_rj3gkm.png)

# Technologies Used

## FrontEnd
+ HTML5
+ CSS3
+ Bootstrap

## BackEnd
+ Django as python web framework for rapid development and clean design.
+ Django Crispy Forms to style django forms.

### Other
+ GitHub to store and share all project code remotely.
+ Balsamiq to create the wireframes for this project.
+ Heroku for deployment

+ Visual Studio Code is the IDE used for developing this project.
+ Stripe as payment platform to validate and accept credit card payments securely.
+ AWS S3 Bucket to store images entered into the database.
+ Boto3 to enable creation, configuration and management of AWS S3.
+ Django Storages a collection of custom storage backends with django to work with boto3 and AWS S3.
+ Gunicorn WSGI HTTP Server for UNIX to aid in deployment of the Django project to heroku.
+ Pillow as python imaging library to aid in processing image files to store in database.
+ Psycopg2 as PostgreSQL database adapter for Python.


+ PIPENV for installation of tools needed in this project.
+ Git to handle version control.
    
    


# Deployment <a name="deploying"></a>

## Run Locally <a name="local"></a>

> In order to run the project locally, you will need an IDE, PIP, Python (version 3) and Git installed.
> You will need to set up a free account with Stripe and with AWS for a S3 bucket.

1. Visit the 2infinity repository on Github; [https://github.com/fdeboo/to-infinity](https://github.com/fdeboo/to-infinity) and click on ![Code](https://res.cloudinary.com/fdeboo/image/upload/v1611914876/toinfinity_readme/clone_trqifl.png) to clone or download it.
2. Either:
***or***

```
  git clone https://github.com/fdeboo/to-infinity.git
```

* Click to **Download Zip** and save the folder somewhere on your local system
    * File > Open the project from within your IDE
    * Copy the web url. In the terminal of your IDE, change directory / `cd` to where you want the project saved on your system.
    * Type `git clone` and paste in the copied web url to complete the command *(as below)*:
3. Activate a virtual environment. For this, I recommend using the **pipenv** package which manages the virtualenv and automatically adds/removes packages to a Pipfile when they are un/installed.

> *NOTE: The Pipfile created by **pipenv** supersedes the requirements.txt*

* Once pipenv insalled, activate it with the following command:
    <code data-te-codeblock="">pipenv shell</code>
    * On MacOS, pipenv is installed simply by typing `brew install pipenv` in the Mac Terminal. You can read more about pipenv and its installation using other software [here](https://pypi.org/project/pipenv/).
4. Install the project dependencies detailed in the Pipfile by typing

```
 pipenv install
```

5. Set up a .env file in the project root and provide the folllowing environment variables:

> *Important! Make sure you set up a .gitignore file and list .env in it so that it is ignored in commits to GitHub*

```
 SECRET_KEY=your_secret_key
 STRIPE_PUBLIC_KEY=your_stripe_public_key
 STRIPE_SECRET_KEY=your_stripe_secret_key
 STRIPE_WH_SECRET=your_stripe_wh_secret
 DEVELOPMENT=True
```

*\*for guidance on where to obtain these values click [here](#guidance)*
6\. If using VSCode\, or else if necessary\, restart the IDE and reactivate the virtual environment \(as per step 3\)
7\. Migrate the admin panel models to create the database template:

```
 python3 manage.py migrate
```

8. Create a 'superuser' account for access to the django admin panel:

```
 python3 manage.py createsuperuser
```

9. Finally, run the app locally with the following command:

```
python3 manage.py runserver
```

## Deploying to Heroku <a name="heroku"></a>

> *NOTE: The Pipfile created by **pipenv** supersedes the requirements.txt and contains all information for the dependencies of the project. Therefore a requirements.txt is not necessary in this project.*

1. Type the following command into the Terminal to create a Procfile:

```
 echo web: python app.py > Procfile
```

2. Change the contents of the Procfile to:

```
 web: gunicorn to_infinity.wsgi:application
```

3. Login to Heroku and click **New** from your Personal dashboard to **Create a New App**.
4. Give the app a unique name and choose the relevant region.
5. In the dashboard for the newly created app, set the **Deployment Method** (found under **Deploy** tab) to Connect to Github.
6. Fill out your Github details and search for your repository. Click to connect.
7. Choose whether you want to deploy Automatically or Manually.
8. Navigate to **Resources** and search for *postgres* in the Add-ons search bar. Choose **Heroku Postgres** from the dropdown.
9. Make sure the 'Plan name' is set to **Hobby Dev - Free**
![Hobby_Dev - Free](https://res.cloudinary.com/fdeboo/image/upload/v1611914876/toinfinity_readme/hobby_dev_ylcbxw.png)
10. Navigate to **Settings** and click on **Reveal Config Vars**.
11. Ensure the following are set:
*\*for guidance on where to obtain these values click [here](#guidance)*
![Heroku Config Vars](https://res.cloudinary.com/fdeboo/image/upload/v1611914878/toinfinity_readme/blurred_heroku_vars_yac2nh.png)

- - -

\#\# Guidance
AWS\_ACCESS\_KEY\_ID:
AWS\_SECRET\_ACCESS\_KEY:
DATABASE\_URL *(for production)*
EMAIL\_HOST\_USER:
EMAIL\_HOST\_PASS (steps are based on gmail server):
SECRET\_KEY:
STRIPE\_PUBLIC\_KEY:
STRIPE\_SECRET\_KEY:
STRIPE\_WH\_SECRET:
USE\_AWS:

- - -

* Set this to True

> Remember to append the path for the checkout to the end of the url, including the trailing '/': `/checkout/wh/`

```
  * Install ngrok. (On MacOs, `brew install ngrok`)
  * Type `ngrok http  8000` in the terminal
  * Add the temporary server address to ALLOWED\_HOSTS in the app settings eg. `[“9e96e1506ea8.ngrok.io”, “127.0.0.1”]`
```

* Click the link alternative to **'receive all events'** in the 'Events to send' section and then 'Add endpoint'
    * Copy the Signing secret provided.
    * As above
    * Copy the Secret Key token
    * Create an account / Sign in to Stripe
    * From the side menu, click on **Developers** > **API Keys**
    * Copy the Publishable Key token
    * Type `python3` in the terminal and then type `import secrets` and hit enter. Type `secrets.token_urlsafe(48)` to generate a secure randomized byte string containing 48 bytes.
    * Sign in to gmail and go to **Settings** > *See all settings*.
    * Navigate to **Accounts & Import** > **Other Google Account Settings.**
    * From the side menu, click on **Security** and follow the steps to turn on 2-Step Verification.
    * Click on **App Passwords**, choose 'Mail' from the first dropdown and 'other' from the second, giving it a reference i.e 'Django'
    * Your gmail account address
    * This value is pre-populated by Heroku in the Config Vars. Alternatively, you can type `Heroku config` in the CLI
    * As above
    * copy the Secret Access Key
    * Create an account / Sign in to AWS and navigate to the **AWS Management Console**
    * Search for S3 in AWS Services and **Create a bucket**. Follow the AWS [documentation.](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/create-configure-bucket.html)
    * Create a User via the IAM service provided by aws
    * As above
    * From the side menu, click on **Developers** > **Webhooks**
    * Click on button to '+ Add endpoint'.
    * Provide your endpoint url. If you are working locally, you may need to take these extra steps for a temporary url:

12. Migrate changes to the database models
13. Commit any changes to GitHub (master branch) and deploy to Heroku. If this is not set to happen automatically, click **Deploy** from Heroku dashboard and navigate to **Manual Deploy** at the bottom of the page. Select the master branch and click **Deploy Branch**.
14. Once the build is complete, click on **Open app** to view the site.

# Bugs <a name="bugs"></a>

1. Circular import issue.  
**Cause:** I initially listed the 'Trip' model within the products app. I imported the 'Booking' model from the bookings app so that I could place an aggregate Query on the Booking objects and use the data returned to update the trip object. In the bookings app, I required the Trip model to be imported and used as a positional argument in a ForeignKey within the Booking model. This resulted in a circular import and caused an Import Error.  
**Solution:** There were a couple of solutions to this issue. One option was to use lazy evaluation and pass products.Trip as a string in the ForeignKey, instead of just defining the model name. This would the alleviate the need to create an import. However, I did not want to use a lazy lookup so as to protect the app's performance. Instead, I reconsidered the arrangement of the models within the app and was able to solve the issue quite easily by moving the Trip model to the booking app and updating the imports as necessary.
2. 'NoneType' object has no attribute 'model'  
**Cause:** When the DateChoiceForm is initialised, the queryset attribute on the ModelChoiceField is overidden with a dynamically generated queryset passed in the \*\*kwargs. If no key is found in the \*\*kwargs, the default value returned is None.
The DateChoiceForm is instantiated again with request.POST when it comes to retrieving the form's POST data. The problem was that the paramater required to initialise the form was not provided. Therefore the kwarg was taking the fallback value of None and subsequently setting the value of the queryset to None.  
**Solution:** I refactored the code so that a view that renders a form in it's get method also handles the form's POST data in it's post method. Since the DateChoiceForm is dynamically rendered using data from the SearchTripsForm, I passed the SearchTripForm's input values to the session so that it could be accessed from the view associated with the DateChoiceForm. Within this view, I created a series of custom class methods to retrieve the data from the session and generate a queryset with it. The class methods were available to view's default get and post method which meant that the DateChoiceForm could be inititalised with the same queryset in both the post and get methods.
3. User model imported from django.contrib.auth.models
This error has been reported [See here](https://github.com/PyCQA/pylint-django/issues/278)

# Credits

## Content

The flow of the form was inspired by [Kenmore Air](https://www.kenmoreair.com)

## Media

The majority of images used in this project were sourced from Pexels. Thanks to [Pixabay](https://www.pexels.com/@pixabay)

## Code

* The [Try DJANGO Tutorial](https://www.youtube.com/watch?v=6oOHlcHkX2U&list=PLEsfXFp6DpzTD1BD1aWNxS2Ep06vIkaeW&index=23) youtube series *(Episode 23-28)*, by Coding Entrepreneurs helped me understand the advantages of Django Forms
* [HTML5 Date Input With Django Forms](https://www.youtube.com/watch?v=I2-JYxnSiB0) by Pretty Printed
* [Inline Formsets](https://dev.to/zxenia/django-inline-formsets-with-class-based-views-and-crispy-forms-14o6)
* 
* Stack overflow
[For forms](https://stackoverflow.com/questions/34781524/django-populate-a-form-choicefield-field-from-a-queryset-and-relate-the-choice-b)
* I based my booking form which used inline\_formets to created a nested fomm, on [this](https://swapps.com/blog/working-with-nested-forms-with-django/) walkthrough tutorial from Swapps.