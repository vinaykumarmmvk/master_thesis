#page_redirect - used to handle button click redirect in same page or new tab
#author - Vinay Kumar Mysuru Manjunath
#github link - https://github.com/vinaykumarmmvk/codeSearch

#Streamlit html component to execute html type
from streamlit.components.v1 import html

#to open url in a new tab
def open_page(url):
    open_script= """
        <script type="text/javascript">
            window.open('%s', '_blank').focus();
        </script>
    """ % (url)
    html(open_script)

#to open url in a same tab
def open_pageself(url):
    open_script= """
        <script type="text/javascript">
            //window.parent.document.body.innerHTML="";
            window.parent.open('%s', '_self');
        </script>
    """% (url)
    html(open_script)