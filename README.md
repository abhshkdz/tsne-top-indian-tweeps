# Visualizing using t-SNE

Visualization of top 100 Indian Twitter accounts using t-SNE.

Source: http://karpathy.github.io/2014/07/02/visualizing-top-tweeps-with-t-sne-in-Javascript/

Credits: [Andrej Karpathy](http://cs.stanford.edu/people/karpathy/)

## Implementation Details

* `data/get_tweets.py` and `data/get_images.py` download tweets and images from Twitter.
* `main.py` creates td-idf vector and calculates distance matrix.
* `index.html` picks up data from `data.json`.