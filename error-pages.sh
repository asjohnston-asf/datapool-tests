HOST=$1
PREFIX=${HOST}/error_doc

/opt/google/chrome/chrome --incognito ${PREFIX}/file_not_found.html
/opt/google/chrome/chrome --incognito ${PREFIX}/data_temporarily_unavailable.html
/opt/google/chrome/chrome --incognito ${PREFIX}/unauthorized.html
/opt/google/chrome/chrome --incognito ${PREFIX}/internal_server_error.html
