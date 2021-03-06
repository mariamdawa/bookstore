from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    paddword2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        field = ["username", 'email', 'password', 'password2']

    def save(self,**kwargs):
        user = User(
            email=self.validated_data.get('email'),
            username=self.validated_data.get('username')
        )
        if self.validated_data.get('password') != self.validated_data.get('password2'):
            raise serializers.ValidationError({
                "password": "Please enter the same password"
            })
        else:
            user.set_password(self.validated_data.get("password"))
            user.save()