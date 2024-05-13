from .views import *
from django.urls import path

urlpatterns=[
    path('notification/',NotificationList.as_view(),name='notification'),
    path('notification/create/',NotificationCreate.as_view(),name='notification-create'),
    path('goalOfTheDay/create/',GoalOfTheDayCreate.as_view(),name='goalOfTheDay-create'),
    path('goalOfTheDay/update/<pk>',GoalOfTheDayUpdate.as_view(),name='goalOfTheDay-update'),
    path('goalOfTheDay/detail/<pk>',GoalOfTheDayDetail.as_view(),name='goalOfTheDay-delail'),
    path("latestActivity/list/",LatestActivitiesList.as_view(),name="latest-activities-list"),
    path("latestActivity/detail/<pk>",LatestActivitiesDetail.as_view(),name="latest-activities-detail"),
    path("latestActivity/create/",LatestActivitiesCreate.as_view(),name="latest-activities-create"),
    path("workout/list/",WorkoutList.as_view(),name="workout-list"),
    path("workout/detail/<pk>",WorkoutDetail.as_view(),name="workout-detail"),
    path("workout/create/",WorkoutCreate.as_view(),name="workout-create"),
    path("exercise/list/",ExerciseList.as_view(),name="exercise-list"),
    path("exercise/detail/<pk>",ExerciseDetail.as_view(),name="exercise-detail"),
    path("exercise/create/",ExerciseCreate.as_view(),name="exercise-create"),
    path("plan/list/",PlanList.as_view(),name="plan-list"),
    path("plan/create/",PlanCreate.as_view(),name="plan-create"),
    path("food/list/",FoodList.as_view(),name="food-list"),
    path("food/detail/<pk>",FoodDetail.as_view(),name="food-detail"),
    path("food/create/",FoodCreate.as_view(),name="food-create"),
    path("recipe/list/",RecipeList.as_view(),name="recipe-list"),
    path("recipe/detail/<pk>",RecipeDetail.as_view(),name="recipe-detail"),
    path("recipe/create/",RecipeCreate.as_view(),name="recipe-create"),
    path("nutrion/list/",NutrionList.as_view(),name="nutrition-list"),
    path("nutrion/detail/<pk>",NutrionDetail.as_view(),name="nutrition-detail"),
    path("nutrion/create/",NutrionCreate.as_view(),name="nutrition-create"),
    path("profile/<pk>/",ProfileDetail.as_view(),name="profile"),
    path('signup/',SignUp.as_view(),name='signup'),
    path('signin/',SignIn.as_view(),name='signin'),
    path('logout/',Logout.as_view(),name='logout'),
    
]