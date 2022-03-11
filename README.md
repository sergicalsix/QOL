# 概要

## TODO
- tailwindcssの軽量化
- QOL検索機能


## startproject

### tailwindcss
```
% npm init -y && npm install tailwindcss autop
refixer clean-css-cli && npx tailwindcss init -p
%
```

### package.json
"scripts": {
"build": "tailwind build ../static/css/tailwind.css -o ../static/css/style.css && cleancss -o ../static/css/style.min.css ../static/css/style.css" 
},