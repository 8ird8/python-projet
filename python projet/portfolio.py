import streamlit as st 
from PIL import Image 
with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# BELAHBIB ACHRAF
#####   *Porftolio* 
''')

image = Image.open('cv.jpg')
st.image(image, width=200)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- Over two years of experience in web design projects, including assembling user requests, generating code, creating mock-ups and enhancing 
                 to impress customers.
                 Focus on creating an impeccable and robust code with exceptional security. Ability to achieve compatibility objectives while meeting and exceeding customer requirements.

''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand"  target="_blank">Belahbib Achraf</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Education
''')

txt('**bacalaureat** (Science Phisique ), *Abdlah Ben Yassine*, inezagane',
'2017')


txt('**Licence** (Siences Phisique,Electronique), * Universitè des Siences Apliquèes ibn Zohr  *, Ait Meloul',
'2018-2021')

#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `php`, `Linux`')
txt3('Data processing/wrangling', '`SQL`')
txt3('Web development', '`Flask`, `HTML`, `CSS`,`jango`,`laravel`')
txt3('Model deployment', '`streamlit`')

#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/achraf-blhabib-422166266/')
txt2('Twitter', 'https://twitter.com/ACHRAFbib')
txt2('Instagram', 'https://www.instagram.com/achraf_blhabib/')
txt2('GitHub', 'https://github.com/8ird8')




