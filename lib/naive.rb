class Naive
  Word = Struct.new(:index, :chars) do
    def length
      chars.length
    end
  end

  def truncate(length, text)
    words = text
      .split(' ')
      .map.with_index { |word, index| Word.new(index, word) }

    loop do
      truncated_text = words.sort_by(&:index).map(&:chars).join(' ')
      return truncated_text if truncated_text.length <= length

      words.sort_by { |word| (word.length * -1) | word.index }.first.tap do |word|
        word.chars = word.chars[0...-1]
      end
    end
  end
end
