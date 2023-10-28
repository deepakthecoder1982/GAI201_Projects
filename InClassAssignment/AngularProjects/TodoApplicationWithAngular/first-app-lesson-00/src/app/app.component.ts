import { Component } from '@angular/core';
import { TestComponent } from './test/test.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    // TestComponent
  ],
  templateUrl:'./app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent {
  title = 'Home';
}


// @Component({
//   selector: 'app-root',
//   templateUrl: './app.component.html',
//   styleUrls: ['./app.component.css'],
// })
// export class AppComponent {
//   title = 'Angular Todo App'; // Update your title here
// }
