require "rspec"
require "./lib/with_dictionary"

describe WithDictionary do
  it "truncates by dictionary lookup" do
    expect(subject.truncate(14, 'small diagonal cross')).to eq('sm diag cross')
  end
end
