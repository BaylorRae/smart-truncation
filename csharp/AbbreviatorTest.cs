using NUnit.Framework;

namespace Tests
{
    public class AbbreviatorTest
    {
        private Abbreviator Subject { get; set; }

        [SetUp]
        public void SetUp() {
            Subject = new Abbreviator();
        }

        [Test]
        [TestCase(14, "small diagonal cross", "sm diag cross")]
        [TestCase(16, "small diagonal cross", "small diag cross")]
        [TestCase(17, "small diagonal cross", "sm diagonal cross")]
        public void Test1(int desiredLength, string input, string expected)
        {
            Assert.That(Subject.AbbreviateToLength(desiredLength, input), Is.EqualTo(expected));
        }
    }
}