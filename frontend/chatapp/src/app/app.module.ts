import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { LoginComponent } from './login/login.component';
import { SignupComponent } from './signup/signup.component';
import { HomeComponent } from './home/home.component';
import { ProfileComponent } from './profile/profile.component';
import { NavbarComponent } from './navbar/navbar.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatButtonModule } from '@angular/material/button';
import { MatInputModule } from '@angular/material/input';
import { MatListModule } from '@angular/material/list';
import { MatCardModule } from '@angular/material/card';
import { MatIconModule } from '@angular/material/icon';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';
import { MatDialogModule } from '@angular/material/dialog';
import { LoadingDialogComponent } from './loading-dialog/loading-dialog.component';
import { MatToolbarModule } from '@angular/material/toolbar';
import { ChatHistoryListComponent } from './chat-history-list/chat-history-list.component';
import { ChatDetailsComponent } from './chat-details/chat-details.component';
import { ChatDataService } from './chat-data.service';

import { MatSidenavModule } from '@angular/material/sidenav';


@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    SignupComponent,
    HomeComponent,
    ChatHistoryListComponent,
    ProfileComponent,
    NavbarComponent,
    LoadingDialogComponent,
    ChatHistoryListComponent,
    ChatDetailsComponent,
    ChatDetailsComponent,
    
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    ReactiveFormsModule,
    HttpClientModule,
    BrowserAnimationsModule,
    MatButtonModule,
    MatInputModule,
    MatListModule,
    MatCardModule,
    MatIconModule ,
    MatProgressSpinnerModule,
    MatDialogModule,
    MatToolbarModule,
    MatSidenavModule
  ],
  providers: [ChatDataService],
  bootstrap: [AppComponent]
})
export class AppModule { }
