//tune for listening state
#define BUZZ_C5  523
#define BUZZ_E5  659


int tempo_buzz = 200;      // change this to make the song slower or faster

int buzzer_buzz = 8;       // change this to whichever pin you want to use

int melody_buzz[] = {

  BUZZ_E5,8, BUZZ_C5,4, 

};

// sizeof gives the number of bytes, each int value is composed of two bytes (16 bits)
// there are two values per note (pitch and duration), so for each note there are four bytes
int notes_buzz = sizeof(melody_buzz) / sizeof(melody_buzz[0]) / 2;
// this calculates the duration of a whole note in ms
int wholenote_buzz = (60000 * 4) / tempo_buzz;
int divider_buzz = 0, noteDuration_buzz = 0;

void buzz()
{
  // iterate over the notes of the melody.
  // Remember, the array is twice the number of notes (notes + durations)
  for (int thisNote_buzz = 0; thisNote_buzz < notes_buzz * 2; thisNote_buzz = thisNote_buzz + 2) {
    // calculates the duration of each note
    divider_buzz = melody_buzz[thisNote_buzz + 1];
    if (divider_buzz > 0) {
      // regular note, just proceed
      noteDuration_buzz = (wholenote_buzz) / divider_buzz;
    } else if (divider_buzz < 0) {
      // dotted notes are represented with negative durations!!
      noteDuration_buzz = (wholenote_buzz) / abs(divider_buzz);
      noteDuration_buzz *= 1.5; // increases the duration in half for dotted notes
    }
    // we only play the note for 90% of the duration, leaving 10% as a pause
    tone(buzzer_buzz, melody_buzz[thisNote_buzz], noteDuration_buzz * 0.9);
    // Wait for the specief duration before playing the next note.
    delay(noteDuration_buzz);
    // stop the waveform generation before the next note.
    noTone(buzzer_buzz);
  }
  
  delay(10);
}
