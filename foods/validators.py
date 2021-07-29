from django.core.exceptions import ValidationError
import re
import phonenumbers

class PhoneValidator:
    requires_context = False
    @staticmethod
    def validate(value):
        try:
            item = phonenumbers.parse("+" + value)
            if not phonenumbers.is_valid_number(item):
                return False
        except:
            return False
        if len(value) !=12 or not value.startswith("998"):
            return False
        return True
    
    def _cal_(self,value):
        if not PhoneValidator.validate(value):
            raise ValidationError("Telefon raqamini tog'ri kiriting...")
