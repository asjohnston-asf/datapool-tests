HOST=$1
PREFIX=${HOST}/error_doc

/opt/google/chrome/chrome --incognito ${PREFIX}/404.html
/opt/google/chrome/chrome --incognito ${PREFIX}/409.html
/opt/google/chrome/chrome --incognito ${PREFIX}/500.html
/opt/google/chrome/chrome --incognito ${PREFIX}/502.html
/opt/google/chrome/chrome --incognito ${PREFIX}/503.html
/opt/google/chrome/chrome --incognito ${PREFIX}/unrestricted/401.html
/opt/google/chrome/chrome --incognito ${PREFIX}/restricted/401.html
/opt/google/chrome/chrome --incognito ${PREFIX}/sentinel/401.html
/opt/google/chrome/chrome --incognito ${PREFIX}/sentinel/403.html
/opt/google/chrome/chrome --incognito ${PREFIX}/palsar/401.html
/opt/google/chrome/chrome --incognito ${PREFIX}/palsar/403.html
