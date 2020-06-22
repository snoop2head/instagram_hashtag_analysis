# instagram_hashtag_analysis
Crawl and Analyze Instagram Hashtag Data

## Header Numbers for files

* 0: Crawl Instagram posts according to search result of #keyword
* 1: Create and wrangle dataset with pandas
* 2: KoNLPy tagging for Koran nouns, Korean action words
* 3: Extract similar documents and make word2Vec models with gensim
* 4: TF-IDF code without using scikit-learn library
* 5: Extracting similar documents using scikit-learn library's tfidfvectorizer

## 문서 앞에 있는 번호는 다음을 의미함
* 0: #keyword 검색, 해시태그 기반 인스타그램 크롤링

* 1: 인스타그램 데이터 통합 및 조작 - Pandas 모듈 이용

* 2: KoNLPy 형태소분석 -> 최대 빈도 체언(명사), 서술어(동사, 형용사) 도출

* 3: Gensim을 이용한 Word2Vec 모델 도출 및 유사 문서 추출

* 4: scikitlearn 모듈을 사용하지 않은, Vanilla로 작성한 TF-IDF 예제

* 5: scikitlearn 모듈의 TF-IDF Vectorizer을 이용한 유사 문서 도출
