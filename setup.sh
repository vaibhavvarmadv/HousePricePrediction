mkdir -p ~/.streamlit/
echo "\
[server]\n\
headless = true\n\
port = 3000\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml
