// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/118666?language=javascript

function solution(survey, choices) {
  var answer = '';

  const characters = ['RT', 'CF', 'JM', 'AN'];

  const result = {
    'R': 0, 'T': 0,
    'C': 0, 'F': 0,
    'J': 0, 'M': 0,
    'A': 0, 'N': 0
  };

  for (let i=0; i < survey.length; i++) {
    if (choices[i] > 4) {
      result[survey[i][1]] += choices[i] - 4;
    } else if (choices[i] < 4) {
      result[survey[i][0]] += 4 - choices[i];
    }
  }

  for (let character of characters) {
    const [char1, char2] = character.split('');
    answer += result[char2] > result[char1] ? char2 : char1;
  }

  return answer
}