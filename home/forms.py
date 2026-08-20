from django import forms

class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=100, label="Họ và tên", error_messages={
        'required': "Vui lòng nhập họ tên của bạn",
        'max_length': "Họ và tên không được quá 100 kí tự"
    })
    email     = forms.EmailField(label="Email liên hệ", error_messages={
        'required': "Vui lòng nhập địa chỉ email của bạn",
        'invalid': "Địa chỉ email không hợp lệ, vui lòng kiểm tra lại. Địa chỉ email nên có dạng name@example.com"
    })
    content   = forms.CharField(widget=forms.Textarea, label="Nội dung", error_messages={
        'required': "Vui lòng nhập nội dung bạn muốn gửi"
    })

    def clean_content(self):
        data = self.cleaned_data['content']
        banned_words = ["lừa đảo", "scam", "rác", "chửi", "chết"]
        for word in banned_words:
            if word in data:
                raise forms.ValidationError("Vui lòng sử dụng ngôn từ lịch sự!")
        return data