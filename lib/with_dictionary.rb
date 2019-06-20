class WithDictionary
  DICTIONARY = {
    'small' => 'sm',
    'diagonal' => 'diag'
  }

  def truncate(length, text)
    words = text.split(' ')

    known_words = words & DICTIONARY.keys
    combinations = known_words.length.times
      .flat_map { |x| known_words.combination(x + 1).to_a }

    versions = []
    combinations.each do |words_to_attempt|
      versions << words.map do |word|
        if words_to_attempt.include?(word)
          DICTIONARY[word]
        else
          word
        end
      end.join(' ')
    end

    versions
      .sort_by(&:length)
      .reverse
      .select { |version| version.length <= length }
      .first
  end
end
