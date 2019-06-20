require "rspec"
require "./lib/with_dictionary"

describe WithDictionary do
  it "trucates closest to desired length" do
    expect(subject.truncate(14, 'small diagonal cross')).to eq('sm diag cross')
    expect(subject.truncate(16, 'small diagonal cross')).to eq('small diag cross')
    expect(subject.truncate(17, 'small diagonal cross')).to eq('sm diagonal cross')
  end
end
