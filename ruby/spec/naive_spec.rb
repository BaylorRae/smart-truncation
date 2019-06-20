require "rspec"
require "./lib/naive"

describe Naive do
  it "truncates longest words until it fits" do
    expect(subject.truncate(14, 'small diagonal cross')).to eq('smal diag cros')
  end
end
