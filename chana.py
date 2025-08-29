import streamlit as st

#st.title("Pensamiento Computacional")

st.sidebar.title("Chana Project")
opciones = st.sidebar.selectbox("Select:",["Intro", "Santos-Granero (2002)", "In the search for correlations", "Datasets", "Expected Outcomes"] )

if opciones == "Intro":
    st.markdown(f'<h2 style="font-size: 42px; text-align: center; ">How are cultural and linguistic traits related geographically and temporally in the Americans?</h2>', unsafe_allow_html=True)
    st.markdown("""
    - Nico Brid
    - Diogo Koga
    - Luisa Gomez
    - Romina Durán
    """)

if opciones == "Santos-Granero (2002)":
    st.markdown(f'<h2 style="font-size: 42px; text-align: center; ">The Arawakan Matrix: Ethos, Language, and History in Native South America</h2>', unsafe_allow_html=True)
    st.markdown("""
    The study of Arawakan peoples in South America seems to reveal that, 
    while the language-culture relationship is not inherently fixed,
    there exists a "common cultural matrix" and a distinctive "ethos" 
    that unites groups within the same linguistic family across time and space.
    It is observed that in vast regions of South America, Arawakan peoples shared an ethos with five key characteristics:
     - Rejection of endo-warfare
     - Propensity for alliances
     - Emphasis on lineage and consanguinity
     - Hereditary leadership and rank
     - Centrality of religion
                
    Despite this persistence of a core ethos for millennia (over 3,000 years), 
    the text shows that intense interactions with non-Arawakan neighbors and historical pressures (e.g., colonial trade) 
    led to the emergence of "transethnic identities."
    In these cases, Arawakan groups could:
     - Maintain their language but adopt a different cultural ethos.
     - Adopt a different language but retain elements of their original Arawakan ethos.
    """)

if opciones == "In the search for correlations":
    st.markdown(f'<h2 style="font-size: 42px; text-align: center; ">In the search for correlations</h2>', unsafe_allow_html=True)
    st.markdown(""" 
    Building upon the Arawakan matrix hypothesis, are cultural and linguistic traits related geographically and temporally in the Americas?  
    Do geographical areas or regions coincide with typological traits and cultural practices?
                

    If so, can they be explained rigorously in terms of cause and effect?
    We take one grammatical trait and one cultural trait as a starting point.
    """)
    st.image("grafico.png")

if opciones == "Datasets":
    st.markdown(f'<h2 style="font-size: 42px; text-align: center; ">Selecting Datasets: Language & Culture</h2>', unsafe_allow_html=True)
    st.markdown("""
    Selection criteria: relevance, representativeness, reliability

    Types of datasets:
    - D-PLACE
    - GeLaTo: Genes and Languages Together
    - Tsammalex
    - WALS
    - GlottoBank (GramBank,NumeralBank, LexicalBank)
    - SAILS

    * Sources: archives, collaborative projects, open digital corpora
    * Goal: connect language and culture.
    """)

if opciones == "Expected Outcomes":
    st.markdown(f'<h2 style="font-size: 42px; text-align: center; ">Expected Outcomes</h2>', unsafe_allow_html=True)
    st.markdown("""
    - A project that can attract Indigenous researchers (e.g., intercultural courses);
    - Elaborating new research tools, such as questionnaires and wordlists with cultural and linguistic specific features;
    - Increasing the quantity of data available on existing datasets;
    - Identifying points of convergence and divergence in cross-linguistic and cross-cultural data analysis, as well as seeking explanations for divergences (including insights from other fields such as genetics);
    - Advancing hypotheses on linguistic and cultural evolution in South America, as well as on their geographical diffusion over time.


    """)


