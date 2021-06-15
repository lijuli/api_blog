path('v1/users/me/', APIUser.as_view()),
    path('v1/auth/email/', RegisterView.as_view(), name='registration'),
    path('v1/auth/token/', MyTokenObtainPairView.as_view(), name='token'),