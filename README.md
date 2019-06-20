# Smart Truncation

1. [Naive Implementation](./lib/naive.rb) [[spec](./spec/naive_spec.rb)]
2. [Dictionary Appraoch](./lib/with_dictionary.rb) [[spec](./spec/with_dictionary_spec.rb)]

Let’s say you have a container with a fixed width and need to truncate text.

```
| small diagonal | cross
```

Traditionally you’d use an ellipsis to truncate the words

```
| small diago... |
```

But a human would abbreviate the words.

```
| sm diag cross  |
```
