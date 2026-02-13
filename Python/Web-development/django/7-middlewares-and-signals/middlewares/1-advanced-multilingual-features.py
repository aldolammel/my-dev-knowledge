"""
File: /core/middlewares.py

    Current features:
    
        - User Authentication Check: It checks if the user is authenticated before processing
                their language preferences.
            
        - Language Preference Handling: If the user is authenticated and has no language
            preference, it sets the user's language based on the current URL's language. If the
            user has a language preference, it activates that language for the request.
        
        - URL Language Redirection: If the URL's language doesn't match the user's preferred
            language, it redirects the user to the same URL with the correct language code.
        
        - Cookie Management: It sets a cookie for non-authenticated users to remember their
            language preference.
        
        - Geolocation Logic: If the user is not authenticated and no language preference is
            found in cookies, it attempts to determine the user's language based on their
            geolocation using their IP address. It maps country codes to specific languages and
            activates the detected language.
        
        - Debugging Information: It prints debugging information about the authenticated user
            and their language preferences when in debug mode.
        
        - Fallback Language Activation: If geolocation fails or if there are issues with the
            API, it falls back to a default language setting.
        
        - Handling of Anonymous Visitors: It manages language preferences for anonymous visitors
            based on their IP address and sets the appropriate language accordingly.
        
        - Request Processing: It processes the request and returns the response after applying
            the language settings.    
"""


import requests
from django.shortcuts import redirect
from django.utils import translation
from django.conf import settings as stg
from accounts.models import Language


def debug_user_authenticated(user, user_lang) -> None:
    """ Debug purposes only. """
    if stg.DEBUG:
        print('\nUSER AUTHENTICATED:')
        print(f'>> User: {user}')
        print('>> External detected IP: not relevant!')
        print('>> Connection Country Code: not relevant!')
        print(f'>> Selected Language: {user_lang} (based on user preference)\n')


class UserLanguageMiddleware:
    def __init__(self, get_response):
        """Dunder method called 'constructor' that runs automatically when a class instance is created."""
        self.get_response = get_response

    def __call__(self, request):
        # First check if user is authenticated:
        if request.user.is_authenticated:
            # Declarations:
            user = request.user
            # Get current URL language:
            current_lang = None
            for lang_code, _ in stg.LANGUAGES:
                if request.path.startswith(f'/{lang_code}/'):
                    current_lang = lang_code
                    break

            # If the user has no language preference, set it based on current URL language:
            if not user.language and current_lang:
                language = Language.objects.get(iso_code=current_lang)
                user.language = language
                user.save()
                translation.activate(current_lang)
                request.LANGUAGE_CODE = current_lang
                # Debug:
                #debug_user_authenticated(user, current_lang)
                #return self.get_response(request)
        
            # Use user's language preference if it exists:
            if user.language:
                user_lang = user.language.iso_code
                translation.activate(user_lang)
                request.LANGUAGE_CODE = user_lang
                
                # Redirect if URL language doesn't match user language:
                for lang_code, _ in stg.LANGUAGES:
                    if request.path.startswith(f'/{lang_code}/') and lang_code != user_lang:
                        # Debug:
                        debug_user_authenticated(user, user_lang)
                        return redirect(request.path.replace(f'/{lang_code}/', f'/{user_lang}/'))
                
                # Update cookie for non-authenticated users
                response = self.get_response(request)
                response.set_cookie(stg.LANGUAGE_COOKIE_NAME, user_lang, max_age=stg.LANGUAGE_COOKIE_AGE)
                # Debug:
                debug_user_authenticated(user, user_lang)
                return response
            
            return self.get_response(request)
                
        # If not authenticated or no language preference in cookies, proceed with geolocation logic:
        if not request.COOKIES.get(stg.LANGUAGE_COOKIE_NAME):
            # Get visitor's IP:
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[0]
            else:
                ip = request.META.get('REMOTE_ADDR')
            # Skip localhost IPs:
            if ip in ('127.0.0.1', 'localhost', '::1'):
                if stg.DEBUG:
                    print('\nANONYMOUS VISITOR:')
                    print(f">> Local development IP detected: {ip}")
                # Get external IP for local development
                try:
                    response = requests.get('https://api.ipify.org?format=json')
                    ip = response.json()['ip']
                except (requests.RequestException, ValueError, KeyError):
                    translation.activate(stg.LANGUAGE_CODE)
                    return self.get_response(request)
            try:
                # Use IP-API for geolocation (free tier):
                response = requests.get(f'http://ip-api.com/json/{ip}')
                data = response.json()
                country_code = data.get('countryCode', '').lower()
                # Map country codes to app languages:
                lang_mapping = {
                    """
                        AI PROMPT:
                        Create a list with all the European countries, other list with all American
                        countries, other list with all Oceania countries and, other list with all
                        African countries, and, the last one, with all Asia countries. Each country
                        is composed of its English name and its ISO country-code (formed by 2
                        characters). Please, separate each continent list by sub-category based on
                        their main/primary language spoken. Consider only those countries where the
                        main/primary language is Portuguese, English, or Spanish.
                    """
                    # America / Portuguese:
                    'br': stg.LANG_CODE_PTBR,
                    # America / Spanish:
                    'ar': stg.LANG_CODE_ES,
                    'bo': stg.LANG_CODE_ES,
                    'cl': stg.LANG_CODE_ES,
                    'co': stg.LANG_CODE_ES,
                    'cr': stg.LANG_CODE_ES,
                    'cu': stg.LANG_CODE_ES,
                    'do': stg.LANG_CODE_ES,
                    'ec': stg.LANG_CODE_ES,
                    'sv': stg.LANG_CODE_ES,
                    'gt': stg.LANG_CODE_ES,
                    'hn': stg.LANG_CODE_ES,
                    'mx': stg.LANG_CODE_ES,
                    'ni': stg.LANG_CODE_ES,
                    'pa': stg.LANG_CODE_ES,
                    'py': stg.LANG_CODE_ES,
                    'pe': stg.LANG_CODE_ES,
                    'pr': stg.LANG_CODE_ES,
                    'uy': stg.LANG_CODE_ES,
                    've': stg.LANG_CODE_ES,
                    # America / English:
                    'ag': stg.LANG_CODE_ENUS,
                    'bb': stg.LANG_CODE_ENUS,
                    'bs': stg.LANG_CODE_ENUS,
                    'bz': stg.LANG_CODE_ENUS,
                    'ca': stg.LANG_CODE_ENUS,
                    'dm': stg.LANG_CODE_ENUS,
                    'gd': stg.LANG_CODE_ENUS,
                    'gy': stg.LANG_CODE_ENUS,
                    'jm': stg.LANG_CODE_ENUS,
                    'kn': stg.LANG_CODE_ENUS,
                    'lc': stg.LANG_CODE_ENUS,
                    'vc': stg.LANG_CODE_ENUS,
                    'tt': stg.LANG_CODE_ENUS,
                    'us': stg.LANG_CODE_ENUS,
                    # Europe / Portuguese:
                    'pt': stg.LANG_CODE_PTBR,
                    # Europe / Spanish:
                    'es': stg.LANG_CODE_ES,
                    # Europe / English:
                    'gb': stg.LANG_CODE_ENUS,
                    'ie': stg.LANG_CODE_ENUS,
                    'mt': stg.LANG_CODE_ENUS,
                    # Africa / Portuguese:
                    'ao': stg.LANG_CODE_PTBR,
                    'mz': stg.LANG_CODE_PTBR,
                    'gw': stg.LANG_CODE_PTBR,
                    'cv': stg.LANG_CODE_PTBR,
                    'st': stg.LANG_CODE_PTBR,
                    'gq': stg.LANG_CODE_PTBR,
                    # Africa / Spanish:
                        # 'gq' also Portuguse and French are official languages, not just spanish.
                    # Africa / English:
                    'ng': stg.LANG_CODE_ENUS,
                    'za': stg.LANG_CODE_ENUS,
                    'ke': stg.LANG_CODE_ENUS,
                    'gh': stg.LANG_CODE_ENUS,
                    'ug': stg.LANG_CODE_ENUS,
                    'tz': stg.LANG_CODE_ENUS,
                    'zm': stg.LANG_CODE_ENUS,
                    'zw': stg.LANG_CODE_ENUS,
                    'mw': stg.LANG_CODE_ENUS,
                    'lr': stg.LANG_CODE_ENUS,
                    'sl': stg.LANG_CODE_ENUS,
                    'bw': stg.LANG_CODE_ENUS,
                    'na': stg.LANG_CODE_ENUS,
                    'sz': stg.LANG_CODE_ENUS,
                    'ls': stg.LANG_CODE_ENUS,
                    'gm': stg.LANG_CODE_ENUS,
                    'mu': stg.LANG_CODE_ENUS,
                    'sc': stg.LANG_CODE_ENUS,
                    'rw': stg.LANG_CODE_ENUS,  # French is official language too.
                    'sd': stg.LANG_CODE_ENUS,
                    'ss': stg.LANG_CODE_ENUS,
                    # Asia / Portuguese:
                    'tl': stg.LANG_CODE_PTBR,
                    # Asia / Spanish:
                        # reserved space.
                    # Asia / English:
                    'in': stg.LANG_CODE_ENUS,
                    'pk': stg.LANG_CODE_ENUS,
                    'ph': stg.LANG_CODE_ENUS,
                    'sg': stg.LANG_CODE_ENUS,
                    'my': stg.LANG_CODE_ENUS,
                    'lk': stg.LANG_CODE_ENUS,
                    'bd': stg.LANG_CODE_ENUS,
                    'bn': stg.LANG_CODE_ENUS,
                    'mv': stg.LANG_CODE_ENUS,
                    'mm': stg.LANG_CODE_ENUS,
                    # Oceania / Portuguese:
                        # reserved space.
                    # Oceania / Spanish:
                        # reserved space.
                    # Oceania / English:
                    'au': stg.LANG_CODE_ENUS,
                    'nz': stg.LANG_CODE_ENUS,
                    'pg': stg.LANG_CODE_ENUS,
                    'fj': stg.LANG_CODE_ENUS,
                    'sb': stg.LANG_CODE_ENUS,
                    'vu': stg.LANG_CODE_ENUS,
                    'ws': stg.LANG_CODE_ENUS,
                    'to': stg.LANG_CODE_ENUS,
                    'ki': stg.LANG_CODE_ENUS,
                    'fm': stg.LANG_CODE_ENUS,
                    'pw': stg.LANG_CODE_ENUS,
                    'mh': stg.LANG_CODE_ENUS,
                    'nr': stg.LANG_CODE_ENUS,
                    'tv': stg.LANG_CODE_ENUS,
                }
                detected_lang = lang_mapping.get(country_code, stg.LANGUAGE_CODE)
                translation.activate(detected_lang)
                request.LANGUAGE_CODE = detected_lang
                # Debug:
                if stg.DEBUG:
                    print(f'>> External detected IP: {ip}')
                    print(f'>> Connection Country Code: {country_code}')
                    print(f'>> Selected Language: {detected_lang} (based on country or cookie)\n')
            # Handle network or API errors:
            except requests.RequestException:
                translation.activate(stg.LANGUAGE_CODE)
            # Handle JSON parsing errors:
            except ValueError:
                translation.activate(stg.LANGUAGE_CODE)
            # Handle missing data in API response:
            except KeyError:
                translation.activate(stg.LANGUAGE_CODE)
        # Otherwise, for visitors with existing cookie (including just logged out users):
        else:
            current_lang = None
            for lang_code, _ in stg.LANGUAGES:
                if request.path.startswith(f'/{lang_code}/'):
                    current_lang = lang_code
                    break
            if current_lang:
                translation.activate(current_lang)
                request.LANGUAGE_CODE = current_lang
        return self.get_response(request)