import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppComponent } from './app.component';
import { TestComponent } from './test/test.component'; // Import your components here

@NgModule({
  declarations: [
    AppComponent,
    TestComponent, // Declare your components here
  ],
  imports: [BrowserModule],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
