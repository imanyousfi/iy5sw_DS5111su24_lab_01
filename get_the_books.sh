
mkdir -P book_dict

BOOK_IDS=("17192" "932" "1063" "10031" "14082")


for BOOK_ID in "${BOOK_IDS[@]}"; do
    wget -P book_dict/ "https://www.gutenberg.org/cache/epub/$BOOK_ID/pg$BOOK_ID.txt" 
done

