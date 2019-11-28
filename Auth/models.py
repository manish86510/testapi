from django.db import models
from django.contrib.auth.models import AbstractUser
from Core.models import SoftDeleteModel

BaseModel = None


class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True, max_length=250)
    salutation = models.CharField(max_length=30, null=True)
    first_name = models.CharField(max_length=150, null=True)
    last_name = models.CharField(max_length=150, null=True)
    about = models.TextField(null=True)
    avatar = models.ImageField(upload_to='avatar/', null=True, blank=True)
    cover_picture = models.ImageField(upload_to='coverPicture/', null=True, blank=True)
    posts_count = models.IntegerField(null=True, blank=True)
    followers_count = models.IntegerField(null=True, blank=True)
    following_count = models.IntegerField(null=True, blank=True)
    skills = models.TextField(null=True)
    address = models.TextField(null=True)
    enlarge_url = models.URLField(null=True)
    date_of_birth = models.DateTimeField(auto_now_add=False, null=True)
    birth_place = models.CharField(max_length=500, null=True)
    gender = models.CharField(max_length=20, null=True)
    is_mail_verified = models.BooleanField(default=False)
    verify_mail_code = models.TextField(max_length=30, null=True, blank=True)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = 'Users'
        db_table = 'User'


class City(SoftDeleteModel):
    city_name = models.CharField(max_length=200)
    city_code = models.CharField(max_length=20)

    def __str__(self):
        return self.city_name

    class Meta:
        verbose_name_plural = 'Cities'
        db_table = 'city'


class WorkPlace(SoftDeleteModel):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    description = models.TextField(null=True)
    working_from = models.DateTimeField(auto_now_add=False)
    working_till = models.DateTimeField(auto_now_add=False)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Work Places'
        db_table = 'work_place'


class Education(SoftDeleteModel):
    school_college_name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    session_from = models.DateTimeField(auto_now_add=False, null=True)
    session_to = models.DateTimeField(auto_now_add=False, null=True)
    attended_for = models.CharField(max_length=200, null=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.school_college_name

    class Meta:
        verbose_name_plural = 'Education'


class MyPlaces(SoftDeleteModel):
    place_name = models.CharField(max_length=200)
    lat_long = models.CharField(max_length=200, null=True)
    from_date = models.DateTimeField(auto_now_add=False, null=True)
    to_date = models.DateTimeField(auto_now_add=False, null=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.place_name

    class Meta:
        verbose_name_plural = 'My Places'
        db_table = 'place'


class SocialLinks(SoftDeleteModel):
    name = models.CharField(max_length=200)
    unique_id = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Social Links'
        db_table = 'social_links'


class MyLanguage(SoftDeleteModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    read = models.CharField(max_length=200, null=True)
    write = models.CharField(max_length=200, null=True)
    speak = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Languages'
        db_table = 'language'


class MyProjects(SoftDeleteModel):
    project_title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    skills = models.TextField(null=True)
    start_date = models.DateTimeField(auto_now_add=False)
    end_date = models.DateTimeField(auto_now_add=False)
    team_size = models.IntegerField(null=True)
    client_name = models.CharField(max_length=200, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.project_title

    class Meta:
        verbose_name_plural = 'My Projects'


class MyInterest(SoftDeleteModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    interest_code = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.interest_code

    class Meta:
        verbose_name_plural = 'My Interest'
        db_table = 'interest'


class MySkills(SoftDeleteModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    skill = models.CharField(max_length=250)


class Followers(SoftDeleteModel):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='follower')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class Interests(models.Model):
    interest = models.CharField(max_length=30)

    # def __str__(self):
    #     return self.interest
    #
    # class Meta:
    #     verbose_name_plural = 'Interests'
    #     db_table = 'all_interest'

    # interest_list = (
    #     ("Yoga", "Yoga"),
    #     ("Theater", "Theater"),
    #     ("Fencing", "Fencing"),
    #     ("Calligraphy", "Calligraphy"),
    #     ("Journaling", "Journaling"),
    #     ("Baking", "Baking"),
    #     ("Stand-up comedy", "Stand-up comedy"),
    #     ("Gardening", "Gardening"),
    #     ("Archery", "Archery"),
    #     ("Language classes", "Language classes"),
    #     ("Camping ", "Camping "),
    #     ("Dancing", "Dancing"),
    #     ("Exploring other cultures", "Exploring other cultures"),
    #     ("Public speaking", "Public speaking"),
    #     ("Volunteering at a charity center", "Volunteering at a charity center"),
    #     ("Local meetups", "Local meetups"),
    #     ("Networking events", "Networking events"),
    #     ("Creating and organizing a book club", "Creating and organizing a book club"),
    #     ("Boardgames", "Boardgames"),
    #     ("Mountain climbing", "Mountain climbing"),
    #     ("Baseball", "Baseball"),
    #     ("Swimming", "Swimming"),
    #     ("Cycling", "Cycling"),
    #     ("Tennis", "Tennis"),
    #     ("Skiing", "Skiing"),
    #     ("Marathon running", "Marathon running"),
    #     ("Volleyball", "Volleyball"),
    #     ("Football", "Football"),
    #     ("Basketball", "Basketball"),
    #     ("Painting", "Painting"),
    #     ("Blog writing", "Blog writing"),
    #     ("Design", "Design"),
    #     ("Photography", "Photography"),
    #     ("Sketching", "Sketching"),
    #     ("Writing", "Writing"),
    #     ("Reading", "Reading"),
    #     ("Playing a musical instrument", "Playing a musical instrument"),
    #     ("Chess", "Chess"),
    # )
    # interest = models.CharField(max_length=30, choices=interest_list, default="Chess")


class Skills(models.Model):
    skill = models.CharField(max_length=30)

    # def __str__(self):
    #     return self.skill
    #
    # class Meta:
    #     verbose_name_plural = 'Skills'
    #     db_table = 'all_skill'
    # skill_list = (
    #     ("Emotional_intelligence", "Emotional_intelligence"),
    #     ("Competitive_spirit", "Competitive_spirit"),
    #     ("Smart_worker", "Smart_worker"),
    #     ("Peaceful", "Peaceful"),
    #     ("Patience", "Patience"),
    #     ("Integrity", "Integrity"),
    #     ("Honesty", "Honesty"),
    #     ("Flexibility", "Flexibility"),
    #     ("Endurance", "Endurance"),
    #     ("Stress_Management", "Stress_Management"),
    #     ("Taking_Criticism", "Taking_Criticism"),
    #     ("Assertiveness", "Assertiveness"),
    #     ("Tolerance", "Tolerance"),
    #     ("Business_etiquette", "Business_etiquette"),
    #     ("Motivating_others", "Motivating_others"),
    #     ("Negotiation", "Negotiation"),
    #     ("Creativity", "Creativity"),
    #     ("Resilience", "Resilience"),
    #     ("Enthusiasm", "Enthusiasm"),
    #     ("Empathy", "Empathy"),
    #     ("Adaptability", "Adaptability"),
    #     ("Jovial", "Jovial"),
    #     ("Self-confidence", "Self-confidence"),
    #     ("Emotion_management", "Emotion_management"),
    #     ("Working_under_pressure", "Working_under_pressure"),
    #     ("Dispute_resolution", "Dispute_resolution"),
    #     ("Interpersonal_relationships", "Interpersonal_relationships"),
    #     ("Crisis_Management", "Crisis_Management"),
    #     ("Diplomacy", "Diplomacy"),
    #     ("Spontaneity", "Spontaneity"),
    #     ("Sense_of_humour", "Sense_of_humour"),
    #     ("Leadership_qualities", "Leadership_qualities"),
    #     ("Creativity", "Creativity"),
    #     ("Adaptability", "Adaptability"),
    #     ("Self_Motivation", "Self_Motivation"),
    #     ("Ability_to_work_in_a_team", "Ability_to_work_in_a_team"),
    #     ("Decision_Making", "Decision_Making"),
    #     ("Time_Management", "Time_Management"),
    #     ("Public_speaking", "Public_speaking"),
    #     ("Filming", "Filming"),
    #     ("Photography", "Photography"),
    #     ("Hardware", "Hardware"),
    #     ("Automotive_repair", "Automotive_repair"),
    #     ("Composer", "Composer"),
    #     ("Graphic_designing", "Graphic_designing"),
    #     ("Schedule_management", "Schedule_management"),
    #     ("Heavy_Machinery_operations", "Heavy_Machinery_operations"),
    #     ("Encryption", "Encryption"),
    #     ("Coding", "Coding"),
    #     ("Testing", "Testing"),
    #     ("Translation", "Translation"),
    #     ("Word_processing", "Word_processing"),
    #     ("Transcription", "Transcription"),
    #     ("Optimization", "Optimization"),
    #     ("Manufacturing", "Manufacturing"),
    #     ("Legal", "Legal"),
    #     ("Bookkeeping", "Bookkeeping"),
    #     ("Accounting", "Accounting"),
    #     ("Critical_thinking", "Critical_thinking"),
    #     ("Analysis", "Analysis"),
    #     ("Multi-lingual", "Multi-lingual"),
    #     ("Word_processing", "Word_processing"),
    #     ("Science", "Science"),
    #     ("Reporting", "Reporting"),
    #     ("Research", "Research"),
    #     ("Project_Management", "Project_Management"),
    #     ("Problem_solving", "Problem_solving"),
    #     ("Mathematics", "Mathematics"),
    #     ("Hardware", "Hardware"),
    #     ("Finance", "Finance"),
    #     ("Data", "Data"),
    #     ("Editing", "Editing"),
    #     ("Writing", "Writing"),
    #     ("Multi-tasking", "Multi-tasking"),
    #     ("Computer_and_Internet_skills", "Computer_and_Internet_skills"),
    #     ("Typing", "Typing"),
    #     ("Certifications", "Certifications"),
    #     ("Web_designing", "Web_designing"),
    #     ("Programming", "Programming"),
    # )
    # skill = models.CharField(max_length=30, choices=skill_list, default="Programming")


class Languages(models.Model):
    language = models.CharField(max_length=30)

    # def __str__(self):
    #     return self.language
    #
    # class Meta:
    #     verbose_name_plural = 'Languages'
    #     db_table = 'all_language'

    # language_list = (
    #     ("Afrikaans", "Afrikaans"),
    #     ("Albanian", "Albanian"),
    #     ("Amharic", "Amharic"),
    #     ("Arabic_(Egyptian_Spoken)", "Arabic_(Egyptian_Spoken)"),
    #     ("Arabic_(Levantine)", "Arabic_(Levantine)"),
    #     ("Arabic_(Modern_Standard)", "Arabic_(Modern_Standard)"),
    #     ("Arabic_(Moroccan_Spoken)", "Arabic_(Moroccan_Spoken)"),
    #     ("Arabic_(Overview)", "Arabic_(Overview)"),
    #     ("Aramaic", "Aramaic"),
    #     ("Armenian", "Armenian"),
    #     ("Assamese", "Assamese"),
    #     ("Aymara", "Aymara"),
    #     ("Azerbaijani", "Azerbaijani"),
    #     ("Balochi", "Balochi"),
    #     ("Bamanankan", "Bamanankan"),
    #     ("Bashkort_(Bashkir)", "Bashkort_(Bashkir)"),
    #     ("Basque", "Basque"),
    #     ("Belarusan", "Belarusan"),
    #     ("Bengali", "Bengali"),
    #     ("Bhojpuri", "Bhojpuri"),
    #     ("Bislama", "Bislama"),
    #     ("Bosnian", "Bosnian"),
    #     ("Brahui", "Brahui"),
    #     ("Bulgarian", "Bulgarian"),
    #     ("Burmese", "Burmese"),
    #     ("Cantonese", "Cantonese"),
    #     ("Catalan", "Catalan"),
    #     ("Cebuano", "Cebuano"),
    #     ("Chechen", "Chechen"),
    #     ("Cherokee", "Cherokee"),
    #     ("Croatian", "Croatian"),
    #     ("Czech", "Czech"),
    #     ("Dakota", "Dakota"),
    #     ("Danish", "Danish"),
    #     ("Dari", "Dari"),
    #     ("Dholuo", "Dholuo"),
    #     ("Dutch", "Dutch"),
    #     ("English", "English"),
    #     ("Esperanto", "Esperanto"),
    #     ("Estonian", "Estonian"),
    #     ("Éwé", "Éwé"),
    #     ("Finnish", "Finnish"),
    #     ("French", "French"),
    #     ("Georgian", "Georgian"),
    #     ("German", "German"),
    #     ("Gikuyu", "Gikuyu"),
    #     ("Greek", "Greek"),
    #     ("Guarani", "Guarani"),
    #     ("Gujarati", "Gujarati"),
    #     ("Haitian_Creole", "Haitian_Creole"),
    #     ("Hausa", "Hausa"),
    #     ("Hawaiian", "Hawaiian"),
    #     ("Hawaiian_Creole", "Hawaiian_Creole"),
    #     ("Hebrew", "Hebrew"),
    #     ("Hiligaynon", "Hiligaynon"),
    #     ("Hindi", "Hindi"),
    #     ("Hungarian", "Hungarian"),
    #     ("Icelandic", "Icelandic"),
    #     ("Igbo", "Igbo"),
    #     ("Ilocano", "Ilocano"),
    #     ("Indonesian_(Bahasa_Indonesia)", "Indonesian_(Bahasa_Indonesia)"),
    #     ("Inuit/Inupiaq", "Inuit/Inupiaq"),
    #     ("Irish_Gaelic", "Irish_Gaelic"),
    #     ("Italian", "Italian"),
    #     ("Japanese", "Japanese"),
    #     ("Jarai", "Jarai"),
    #     ("Javanese", "Javanese"),
    #     ("K’iche’", "K’iche’"),
    #     ("Kabyle", "Kabyle"),
    #     ("Kannada", "Kannada"),
    #     ("Kashmiri", "Kashmiri"),
    #     ("Kazakh", "Kazakh"),
    #     ("Khmer", "Khmer"),
    #     ("Khoekhoe", "Khoekhoe"),
    #     ("Korean", "Korean"),
    #     ("Kurdish", "Kurdish"),
    #     ("Kyrgyz", "Kyrgyz"),
    #     ("Lao", "Lao"),
    #     ("Latin", "Latin"),
    #     ("Latvian", "Latvian"),
    #     ("Lingala", "Lingala"),
    #     ("Lithuanian", "Lithuanian"),
    #     ("Macedonian", "Macedonian"),
    #     ("Maithili", "Maithili"),
    #     ("Malagasy", "Malagasy"),
    #     ("Malay_(Bahasa_Melayu)", "Malay_(Bahasa_Melayu)"),
    #     ("Malayalam", "Malayalam"),
    #     ("Mandarin_(Chinese)", "Mandarin_(Chinese)"),
    #     ("Marathi", "Marathi"),
    #     ("Mende", "Mende"),
    #     ("Mongolian", "Mongolian"),
    #     ("Nahuatl", "Nahuatl"),
    #     ("Navajo", "Navajo"),
    #     ("Nepali", "Nepali"),
    #     ("Norwegian", "Norwegian"),
    #     ("Ojibwa", "Ojibwa"),
    #     ("Oriya", "Oriya"),
    #     ("Oromo", "Oromo"),
    #     ("Pashto", "Pashto"),
    #     ("Persian", "Persian"),
    #     ("Polish", "Polish"),
    #     ("Portuguese", "Portuguese"),
    #     ("Punjabi", "Punjabi"),
    #     ("Quechua", "Quechua"),
    #     ("Romani", "Romani"),
    #     ("Romanian", "Romanian"),
    #     ("Russian", "Russian"),
    #     ("Rwanda", "Rwanda"),
    #     ("Samoan", "Samoan"),
    #     ("Sanskrit", "Sanskrit"),
    #     ("Serbian", "Serbian"),
    #     ("Shona", "Shona"),
    #     ("Sindhi", "Sindhi"),
    #     ("Sinhala", "Sinhala"),
    #     ("Slovak", "Slovak"),
    #     ("Slovene", "Slovene"),
    #     ("Somali", "Somali"),
    #     ("Spanish", "Spanish"),
    #     ("Swahili", "Swahili"),
    #     ("Swedish", "Swedish"),
    #     ("Tachelhit", "Tachelhit"),
    #     ("Tagalog", "Tagalog"),
    #     ("Tajiki", "Tajiki"),
    #     ("Tamil", "Tamil"),
    #     ("Tatar", "Tatar"),
    #     ("Telugu", "Telugu"),
    #     ("Thai", "Thai"),
    #     ("Tibetic_languages", "Tibetic_languages"),
    #     ("Tigrigna", "Tigrigna"),
    #     ("Tok_Pisin", "Tok_Pisin"),
    #     ("Turkish", "Turkish"),
    #     ("Turkmen", "Turkmen"),
    #     ("Ukrainian", "Ukrainian"),
    #     ("Urdu", "Urdu"),
    #     ("Uyghur", "Uyghur"),
    #     ("Uzbek", "Uzbek"),
    #     ("Vietnamese", "Vietnamese"),
    #     ("Warlpiri", "Warlpiri"),
    #     ("Welsh", "Welsh"),
    #     ("Wolof", "Wolof"),
    #     ("Xhosa", "Xhosa"),
    #     ("Yakut", "Yakut"),
    #     ("Yiddish", "Yiddish"),
    #     ("Yoruba", "Yoruba"),
    #     ("Yucatec", "Yucatec"),
    #     ("Zapotec", "Zapotec"),
    #     ("Zulu", "Zulu"),
    # )
    # language = models.CharField(max_length=30, choices=language_list, default="English")
