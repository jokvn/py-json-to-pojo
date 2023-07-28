# json-to-pojo

This is a small python script that converts JSOn data into a Java POJO.

## How to use

### Get more info about the CLI parameters

```sh
python3 jtp.py --help
```

### Run the script

```sh
python3 jtp.py test.json out.java
```

## Output

### test.json

```sh
python3 jtp.py test.json out.java --getter-setter
```

```java
public class MainClass {
	private List<Pets> pets;

	public List<Pets> getPets() {
		return pets;
	}

	public void setPets(List<Pets> pets) {
		this.pets = pets;
	}

}

public class PetsElement {
	private String name;
	private String species;
	private List<String> favFoods;
	private int birthYear;
	private String photo;

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getSpecies() {
		return species;
	}

	public void setSpecies(String species) {
		this.species = species;
	}

	public List<String> getFavfoods() {
		return favFoods;
	}

	public void setFavfoods(List<String> favFoods) {
		this.favFoods = favFoods;
	}

	public int getBirthyear() {
		return birthYear;
	}

	public void setBirthyear(int birthYear) {
		this.birthYear = birthYear;
	}

	public String getPhoto() {
		return photo;
	}

	public void setPhoto(String photo) {
		this.photo = photo;
	}

}
```

### test2.json

```sh
python3 jtp.py test2.json out.java --getter-setter
```

```java
public class MainClass {
	private Quiz quiz;

	public Quiz getQuiz() {
		return quiz;
	}

	public void setQuiz(Quiz quiz) {
		this.quiz = quiz;
	}

}

public class Quiz {
	private Sport sport;
	private Maths maths;

	public Sport getSport() {
		return sport;
	}

	public void setSport(Sport sport) {
		this.sport = sport;
	}

	public Maths getMaths() {
		return maths;
	}

	public void setMaths(Maths maths) {
		this.maths = maths;
	}

}

public class Sport {
	private Q1 q1;

	public Q1 getQ1() {
		return q1;
	}

	public void setQ1(Q1 q1) {
		this.q1 = q1;
	}

}

public class Q1 {
	private String question;
	private List<String> options;
	private String answer;

	public String getQuestion() {
		return question;
	}

	public void setQuestion(String question) {
		this.question = question;
	}

	public List<String> getOptions() {
		return options;
	}

	public void setOptions(List<String> options) {
		this.options = options;
	}

	public String getAnswer() {
		return answer;
	}

	public void setAnswer(String answer) {
		this.answer = answer;
	}

}



public class Maths {
	private Q1 q1;
	private Q2 q2;

	public Q1 getQ1() {
		return q1;
	}

	public void setQ1(Q1 q1) {
		this.q1 = q1;
	}

	public Q2 getQ2() {
		return q2;
	}

	public void setQ2(Q2 q2) {
		this.q2 = q2;
	}

}

public class Q1 {
	private String question;
	private List<String> options;
	private String answer;

	public String getQuestion() {
		return question;
	}

	public void setQuestion(String question) {
		this.question = question;
	}

	public List<String> getOptions() {
		return options;
	}

	public void setOptions(List<String> options) {
		this.options = options;
	}

	public String getAnswer() {
		return answer;
	}

	public void setAnswer(String answer) {
		this.answer = answer;
	}

}


public class Q2 {
	private String question;
	private List<String> options;
	private String answer;

	public String getQuestion() {
		return question;
	}

	public void setQuestion(String question) {
		this.question = question;
	}

	public List<String> getOptions() {
		return options;
	}

	public void setOptions(List<String> options) {
		this.options = options;
	}

	public String getAnswer() {
		return answer;
	}

	public void setAnswer(String answer) {
		this.answer = answer;
	}

}
```

Json example files were taken from https://github.com/LearnWebCode/json-example/tree/master