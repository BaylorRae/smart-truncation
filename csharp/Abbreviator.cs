using System.Linq;
using System.Collections.Generic;

public class Abbreviator
{
  private Dictionary<string, string> Abbreviations = new Dictionary<string, string>
  {
    ["small"] = "sm",
    ["diagonal"] = "diag"
  };

  public string AbbreviateToLength(int desiredLength, string input) {
    var words = input.Split(' ');
    var knownWords = words.Where(word => Abbreviations.ContainsKey(word));
    var combinations = new List<IEnumerable<string>>();

    for (var i = 1; i <= knownWords.Count(); i++) {
      combinations.AddRange(knownWords.Combination(i));
    }

    var variants = new List<string> { input };
    foreach (var combination in combinations) {
      variants.Add(string.Join(' ', words.Select((word) => combination.Contains(word) ? Abbreviations[word] : word)));
    }
    
    return variants
      .OrderByDescending(variant => variant.Length)
      .Where(variant => variant.Length <= desiredLength)
      .First();
  }
}

internal static class CombinationExtension {
  // https://stackoverflow.com/a/33336576/467546
  internal static IEnumerable<IEnumerable<T>> Combination<T>(this IEnumerable<T> ary, int num) {
    return num == 0
      ? new[] { new T[0] }
      : ary.SelectMany((x, i) => ary.Skip(i + 1).Combination(num - 1).Select(y => (new[] {x}).Concat(y)));
  }
}