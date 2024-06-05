
mkdir -P book_dict

BOOK_IDS=("17192" "2148" "2147" "932" "1064" "25525" "10031" "2151" "32037")


for BOOK_ID in "${BOOK_IDS[@]}"; do
    wget -P book_dict/ "https://www.gutenberg.org/cache/epub/$BOOK_ID/pg$BOOK_ID.txt" 
done

