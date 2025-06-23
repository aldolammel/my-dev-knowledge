# from django.utils.translation import gettext_lazy as _

# Reminder: gettext_lazy doesn't work with dynamic compositions _(str) % {dict}, so don't in here!

# SECTION NAMES & NAV GROUPERS: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
"""Summary:
    _NAME = Official section name callable in the content;
    _TTL = Exclusive text for page title;
    _NAV = Exclusive text for navegation;
    _DT = Detail page;    
"""
# General Sections (S_G_):
S_G_HOME_1_NAME = "Pessoal"
S_G_HOME_1_TTL = "Para Você"
S_G_HOME_1_NAV = "Para você"

S_G_REG_NAME = "Criar Conta"
S_G_REG_TTL = "Criar Conta"
S_G_REG_NAV = "Criar conta"

S_G_LOGIN_NAME = "Entrar"
S_G_LOGIN_TTL = "Acesso Seguro"
S_G_LOGIN_NAV = "Entrar"

S_G_LOGIN_RESET_NAME = "Redefinir Senha"
S_G_LOGIN_RESET_TTL = "Redefinindo Senha"
S_G_LOGIN_RESET_NAV = "Redefinir senha"

S_G_LOGIN_RESET_COMPLETE_TTL = "Senha Atualizada"

S_G_ABOUT_NAME = "Sobre"
S_G_ABOUT_TTL = "Sobre <NomeClient/Portal>"
S_G_ABOUT_NAV = "Sobre"

S_G_HELP_NAME = "Perguntas Frequentes"
S_G_HELP_TTL = "Perguntas Frequentes"
S_G_HELP_NAV = "Perguntas Frequentes"

S_G_PRIVACY_NAME = "Política de Privacidade"
S_G_PRIVACY_TTL = "Nossa Política de Privacidade"
S_G_PRIVACY_NAV = "Política de privacidade"

# Logged-In Sections (S_I_):
S_I_HOME_1_NAME = "Resumo"
S_I_HOME_1_TTL = "Resumo"
S_I_HOME_1_NAV = "Meu resumo"

"""S_I_ATTK_LIST_NAME = "Attack Notes"
S_I_ATTK_LIST_TTL = "Attack Notes"
S_I_ATTK_LIST_NAV = "Attacks" """

S_I_PROFILE_NAME = "Perfil"
S_I_PROFILE_TTL = "Perfil"
S_I_PROFILE_NAV = "Meu perfil"

S_I_PROFILE_PWD_NAME = "Mudar Senha"
S_I_PROFILE_PWD_TTL = "Mudando Senha"
S_I_PROFILE_PWD_NAV = "Mudar senha"

# Nav Groupers (NAV_GPR_):
"""NAV_GPR_NOTES_NAV = "My notes"
NAV_GPR_NOTE_NAV = "Take note" """

# LABELS: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
LB_CREATED_AT = "Criado em"
LB_CREATED_BY = "Criado por"
LB_UPDATED_AT = "Atualizado em"
LB_UPDATED_BY = "Atualizado por"
LB_STATUS_CONTENT = "Situação"
LB_NAME = "Nome"
LB_DESCRIPT = "Descrição"
LB_ICON = "Ícone"
LB_COLOR_CSS = "Cor CSS Classname"
LB_IMG = "Imagem"
LB_PHONE_NUMBER = "Número Telefônico"
LB_PHONE_OWNER = "Proprietário"
# LB_LANG_INTERFACE = "Idioma da Interface"
LB_PROFILE_TYPE = "Tipo de Perfil"
LB_PROFILE_PWD_1 = "Senha"
LB_PROFILE_PWD_2 = "Confirmação da Senha"
LB_USER = "Nome de usuário"
LB_USER_PROFILE_LINK = "Você está logado como"
LB_USER_EMAIL = "E-mail"
LB_USER_NOTIF_BY_EMAIL = "Receber Notificação por E-mail"
LB_USER_AGE_MIN = "Tenho 13 anos ou mais"
LB_USER_PRIVACY = "Concordo com a Política de Privacidade"  # TODO
# LB_USER_LANG = "Meu Idioma"
LB_USER_PWD_LAST_UPDATE = "Senha, Última Atualização"
LB_USER_PWD_OLD = "Senha Antiga"
LB_USER_PWD_NEW = "Nova Senha"
LB_USER_PWD_NEW_CONF = "Confirmação da Nova Senha"
LB_PROFILES_USER = "Usuário"
LB_PROFILES_NOTIF_BY_PHONE = "Notificação por Celular"
LB_PROFILE_1_FNAME = "Nome"
LB_PROFILE_1_LNAME = "Sobrenome"
LB_PROFILE_1_SEX = "Sexo Biológico"
LB_PROFILE_1_BIRTHDATE = "Data de Nascimento"
LB_PROFILE_1_BIRTH_YEAR = "Ano de Nascimento"

# FORM BUTTONS: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
BT_REG_SUBMIT = "Criar minha conta"
BT_REG_NEW_ACCOUNT = "Criar nova conta"
BT_PROFILE_LOGOUT = "Sair"
BT_PROFILE_DEL = "Encerrar conta"
BT_PROFILE_SUBMIT = "Salvar mudanças"
BT_PROFILE_PWD_CHANGE = "Mudar senha"
BT_PROFILE_PWD_SUBMIT = BT_PROFILE_PWD_CHANGE
BT_LOGIN = "Entrar"
BT_LOGIN_HAVE_ACCOUNT = "Tenho uma conta"
BT_LOGIN_RESET = "Redefinir senha"
BT_LOGIN_RESET_SUBMIT = "Enviar e-mail de confirmação"
BT_STEP_BACK = "Passo anterior"
BT_STEP_NEXT = "Próximo passo"
BT_DRAFT = "Salvar e finalizar depois"
BT_DISCARD = "Descartar tudo"
BT_CANCEL = "Cancelar"
BT_BACK = "Voltar"
BT_DONE = "Finalizar"

# FORM FEEDBACKS: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
"""TX_FDBK_ATTK_SUCC = "Attack note successfully updated!"
TX_FDBK_ATTK_FAIL = "Oops. Something wrong with your attack note data..."
TX_FDBK_ATTK_DEL = "Your attack note has been deleted."
TX_FDBK_LOGIN_RESET = "If an account exists with the provided e-mail, a password reset link will be sent. Please check your inbox."
TX_FDBK_PROFILE_SUCC_UPDATED = "Profile was updated successfully!"
TX_FDBK_PROFILE_PWD_UPDATED = "Your password was changed successfully."
TX_FDBK_PROFILE_PWD_EQUAL_OLD = "You tried to use the old password as the new one."
TX_FDBK_PROFILE_FAIL = "Oops. Something wrong with your profile data..."
TX_FDBK_PROFILE_1_DEL = "Done! Your account is now blocked and it'll be completely and automatically deleted within 30 days. Thanks for being with us." """

# REPORT (PDF): - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#LB_REPORT_ATTK_TTL = "Attack Report"
#LB_REPORT_ENDED = "ends here."


# FORM ERRORS: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
TX_ERRO_USER_PROFILE_BLNK = "This field is required."  # TODO
TX_ERRO_USER_EMAIL_BLNK = "This field is required."  # TODO
TX_ERRO_USER_EMAIL_INVLD = "Enter a valid e-mail address."
TX_ERRO_USER_AGE_MIN = "To use our services, you must be 13 years or older."  # TODO
TX_ERRO_USER_PRIVACY = "To use our services, you must read and accept our Privacy Policy."  # TODO
TX_ERRO_PROFILE_1_FNAME_MAXLNGH = "This field cannot exceed %(val)s characters."  # TODO
TX_ERRO_PROFILE_1_LNAME_MAXLNGH = "This field cannot exceed %(val)s characters."  # TODO
TX_ERRO_PROFILE_1_BIRTH_MIN = "To protect children and prevent their exposure, the minimum age for using our service is 13 years old."  # TODO
TX_ERRO_PROFILE_1_BIRTH_MAX = "Check the birth year!"
TX_ERRO_PROFILE_1_BIRTH_INVLD = "Invalid date for birthdate."
TX_ERRO_PROFILE_1_SEX_BLNK = "This field is required."  # TODO
"""TX_ERRO_ATTK_START_D_BLNK = "This field is required."
TX_ERRO_ATTK_START_D_LATE = "It doesn't make sense for the start date to be after the end date."
TX_ERRO_ATTK_START_D_INVLD = "Enter a valid Start Date: mm/dd/yyyy."  # TODO this solution isnt good enough!
TX_ERRO_ATTK_START_D_BACK = "The limit for retroactive attack note is 180 days from the current date."  # TODO
TX_ERRO_ATTK_START_D_DUPLICAT_A = "There's another note (which seems still ongoing) in the same period you're trying to record now."
TX_ERRO_ATTK_START_D_DUPLICAT_B = "You're trying to make a note about another one that covers the same period." """

# REGULAR TEXTS WITH OR WITHOUT HYPERLINK: - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
TX_PROFILE_1 = "Pessoal"
TX_PROFILE_1_CTA = "xxxxxxxxxxxxxxxxx"

# GENERIC COMPOSITION TEXTS: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
TX_BY = "by"
TX_FROM = "from"
TX_TO = "to"
TX_YES = "yes"
TX_NO = "no"

# TO SPECIAL USAGE TEXTS:
# Caution: this is used as remider/suffix in other texts. Keep it up-to-date!
TX_PRIVACY_ALERT = "Your personal data such as full name, e-mail and/or phone number are never shared."

# FORM HELPERS: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
TX_HELP_USER_PROFILE = "Define which profile type you'll use on the platform (Personal profile is highly recommended)."
TX_HELP_USER_EMAIL = "We do NOT share your e-mail under any circumstances."
TX_HELP_USER_NOTIF_EMAIL = "Whether you should receive important (non-ad) notifications from your account via e-mail."
#TX_HELP_USER_LANG = "Your favorite language for the <AppName> interface."  # TODO
#TX_HELP_USER_LANG_ISO = "Only 2 characters for original language country. Or 5 for language variation. Use minimal 2 (en, es, pt), maximum 5 (en-us, es-mx, pt-br)."
TX_HELP_USER_AGE_MIN = TX_ERRO_USER_AGE_MIN
TX_HELP_USER_PRIVACY = TX_ERRO_USER_PRIVACY
# TX_HELP_PROFILE_PWD1 =   # Using the Django solution for this!
TX_HELP_PROFILE_PWD2 = "Enter the same password as before, for verification."
TX_HELP_PROFILE_1_NAME = "A name or nickname that you like."
TX_HELP_PROFILE_1_BIRTHDATE = "Your age is valuable to better understand the behavior of headaches over the years."
TX_HELP_PROFILE_1_SEX = "For clinical and <AppName> understanding is crucial to get to know which is your birth sex."
TX_HELP_CREATED_BY = "User who created this record."
TX_HELP_UPDATED_BY = "User who made the most recent update to this record."
TX_HELP_STATUS_CONTENT = "Whether or not this content should be visible to users."
"""TX_HELP_ATTK_CLINIC_VAL = "Current scientific value of this note. The value changes according to the amount of data entered. The more information added, the greater the value for your doctor and our partner research centers."
TX_HELP_ATTK_START_D = "The date when the attack started."
TX_HELP_ATTK_START_T = "The time when the attack started."
TX_HELP_ATTK_WAS_SLEEP = "Check if the attack got started during sleep."
TX_HELP_ATTK_IS_GO = "Check if the attack still going on."
TX_HELP_ATTK_END_D = "The date when the attack finished."
TX_HELP_ATTK_END_T = "The time when the attack finished."
TX_HELP_ATTK_DURATION = "How long the attack was felt."
TX_HELP_ATTK_TYPE = "Type of attack you believe this note is treating."
TX_HELP_ATTK_INTENS = "Highest peak of pain the attack reached."
TX_HELP_ATTK_AREA = "Area(s) of the body where the attack occurred."
TX_HELP_ATTK_MEDICINE = "Medicine(s) used to treat the attack." """

# E-MAIL SUBJECTS: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# SUBJ_RESET_PWD = "<PortalName> password reset"

# CMS ONLY: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
CMS_MORE_DETAILS = "Maid detalhes"
CMS_ERRO_PROFILE = "ERROR: SEM PERFIL!"
"""CMS_LB_ATTK_INFO_CORE = "Core Details"
CMS_LB_ATTK_INFO_RELATED = "Related Information"
CMS_LB_ATTK_INFO_META = "Metadata" """
