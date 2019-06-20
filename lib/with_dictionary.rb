class WithDictionary
  DICTIONARY = {
    'small' => 'sm',
    'diagonal' => 'diag'
  }

  def truncate(length, text)
    text.split(' ').map { |word| DICTIONARY.fetch(word, word) }.join(' ')
  end
end
