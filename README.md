# Smart Truncation

- [Naive Implementation][#1]
- [Dictionary Implementation][#2]

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

## Implementations

### 1. Naive Implementation

The first implementation was a proof of concept to shorten the longest words
first. This would eventually be combined with [#2] to remove any additional
characters.

[naive.rb](./ruby/lib/naive.rb) | [naive_spec.rb](./ruby/spec/naive_spec.rb)

```
| smal diag cros |
```

### 2. Dictionary Implementation

The second approach utilizes a map of known abbreviations. This example has
a few more test cases to find the best replacements to match the desired length.

[with_dictionary.rb](./ruby/lib/with_dictionary.rb) | [with_dictionary_spec.rb](./ruby/spec/with_dictionary_spec.rb)

```
// 14 chars
  1..........14
| sm diag cross     |

// 16 chars
  1.............16
| small diag cross  |

// 17 chars
  1..............17
| sm diagonal cross |
```

## Thanks

Huge thanks to [@wesdoyle] for looking at this problem and offering solutions.

[#1]: #1-naive-implementation
[#2]: #2-dictionary-implementation
[@wesdoyle]: https://github.com/wesdoyle
