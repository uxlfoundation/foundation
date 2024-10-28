=========================================
Math Special Interest Group Meeting Notes
=========================================

2024-10-02
==========

Materials:

* `Discussion on DFT APIs <presentations/UXL-Math-SIG-2024-10-02_RaphaelEgan_set_get_value.pdf>`__
* `Updates <presentations/UXL-Math-SIG-2024-10-02_SarahKnepper_Update.pdf>`__

Attendees:

* Andrey Alekseenko (KTH Royal Institute of Technology)
* Abhishek Bagusetty (Argonne National Laboratory, ANL)
* Romain Biessy (Codeplay)
* Rod Burns (Codeplay)
* Raphael Egan (Intel)
* Akhil Goel (Intel)
* Mehdi Goli (Codeplay)
* Dai-Ni Hsieh (Intel)
* Louise Huot (Intel)
* Sarah Knepper (Intel)
* Maria Kraynyuk (Intel)
* Piotr Luszczek (UTK)
* Kumudha Narasimhan (Codeplay)
* Chris Reed (GE Healthcare)
* Alison Richards (Intel)
* Nicolò Scipione (Codeplay)
* Paolo (Codeplay)


Agenda:

* Discussion on Discrete Fourier Transform APIs - Raphael Egan
* Updates from last meeting - Sarah Knepper

Overview of Discrete Fourier Transform APIs {s,g}et_value member functions - Raphael Egan:

* Thanks for accommodating the date shift for this topic; we want to include this in the upcoming release of the specification.
* We want to talk about improvements especially about type safety for the configuration, setting, and querying member functions of the descriptor class template of the oneMKL element of the oneAPI specification.
* Those member functions are variadic, which triggers confusion about how they are supposed to be used. It is not really the most C++-like approach. They prevent an implementation from enforcing a strict input validation.
* Most critically, there is an issue in the specification itself for an implementation to align with it. We will go into further details of the issues, rootcause, and what I think is a possible path forward.

Targeted scope:

* Say you want to compute a 2-D real transform batched 5 times, using an externally allocated workspace, out-of-place. This configuration requires many configuration parameters to be set explicitly since they are different than default values.
* First you create the descriptor. According to the specification, you should set strides of type std::vector<std::int64_t>. But those set_value functions are declared as variadic, and non-POD data can't be passed in variadic lists.
* The number of transforms should be passed as std::int64_t. Many implementations could handle a literal integer (seemingly) accurately, so long as it is positive, but technically it is undefined behavior and should be cast.
* A parameter whose bounds are a floating point value, like forward_scale, should be passed as an explicit float for single precision.
* The most important point is that vector-valued configuration parameters, like strides, cannot be set correctly because it's not a plain old datatype - this simply cannot be implemented.

What has been done instead:

* Instead of using the vectors for strides (what the specification dictates), implementations have used an array instead; an array of 4 integers in this example, the rank of the descriptor plus one. That's been used for anything that requires a vector.
* Another thing that's been used is to accept a literal value for the 64-bit integer value. Typically there is no error, at least for positive values; if trying to pass a negative integer value, there can be disastrous implications.
* For single precision descriptors, the floating point values should be the same precision (float), but usually still works if a double is passed.

Rootcause:

* The root cause lies in the declaration of the set_value and get_value functions being variadic.
* The specification explicitly states that no more than 2 arguments are expected, and that the second argument should be for setting a value of a given type that depends on the parameter being set.
* The type of the parameter to get or be writable depends on the config_param type.
* For an integer parameter, the expected type is actually 64-bit integer. However, any non-64-bit integer that would be passed would be implicitly promoted to a regular integer, not a 64-bit integer.
* When it comes to the backward and forward scales, the type that is specified in the specification is the real scalar type.
* The implicit promotion for any element of a variadic list will make that irrelevant in the end, because everything would be promoted to a double.
* Most important and critical part is for the \*_STRIDES - the configuration value is expected to be a vector, but it cannot be implemented for set_value because vector types are not plain old data types (PODs).

Proposal:

* Suggesting some changes to specification itself to resolve the inconsistencies and concerns.
* Go around these issues by using configuration-setting member functions.
* Deprecate the variadic set_value member function. No real reason in C++ to use variadic functions. Only reason historically was to handle several different types, ala a C implementation.
* Introduce overloaded alternative versions - the functions in blue and green color would be added to capture intended usage.
* The red one captures what has been used (passing an array to set the strides) - add it as an entry point in the deprecation period to capture the very unclear usage that was allowed, but with a message of what to use instead.
* Blue functions look odd but are needed (SFINAE entry points); without them, we would get compiler ambiguity error. The literal r-value being passed would be considered an integer; it should be promoted to something, and the compiler finds 2 that are equivalent. A single integer value can be promoted equally validly to a 64-bit integer or a floating-point value.
* Other suggestions related to this proposal are that with the newly enabled entry points, we now have strict input validation that should be enabled, with exceptions thrown for invalid input.

* Andrey Alekseenko: The proposal is good because it preserves the legacy syntax. If we are talking about redesign, why not make the config_param a template parameter and also have compile-time validation?

  * Raphael: That has been considered. However, such an implementation requires the parameter to be known at compile time, but this is not always the case.
  * Andrey: Quite common that you'd know it, right?
  * Raphael: Common but not general.
  * Andrey: Why not allow both?
  * Raphael: You're suggesting on top of the current suggestion?
  * Andrey: I was initially thinking instead, but if runtime is an important use case, then on top of. If you're setting forward/backward strides, those wouldn't be known at compile time perhaps and could be handled by user.
  * Raphael: I don't see a reason not to add another entry point that would be fully-templated. I'm not personally against that, but it is going one step further than this. This focus here was to resolve any type-safety related concerns and undefined behavior that might happen.
  * Andrey: You're suggesting to improve type detection at run time, while what I'm saying will improve it at compile time.
  * Raphael: It is more robust, yes. We may consider adding it to the specification.

* Romain Biessy: I was thinking about this as well while you were presenting. Probably it makes sense, but we'd have to see for users with this transition.

  * Raphael: I remember that someone previously at Codeplay brought this up in a pull request; they found some arguments that might have been concerning, and finally concluded that it might have been best not to go fully templated types. I'll make sure if I add this to the specification, it can be safely done. If not, we can discuss this more on the pull request.
  * Andrey: That would be okay with me.

Configuration querying:

* For get_value, the approach is very similar. Add a const qualifier to every get_value function because they are accessors of some kind and are not modifying the descriptor itself. But if we add const to the variadic version, that would break backward compatibility in other implementations. (In the Intel oneMKL product, we allowed ourselves to break backward compatibility in a major release.)
* The idea here would be to enable usage for any integer-valued parameter, but perhaps during the deprecation period an implementation should emit a runtime warning for value_ptr; the main reason being that there's no way for the implementation to guarantee that the value_ptr is pointing to the 0th address of a valid array.

Q&A:

* Romain: If we go with this, does get_value still return void or should it return something else?

  * Raphael: With simple overloading, you can't differentiate just on return type.
  * Romain: I guess if we make them template parameters...
  * Raphael: If we go with that, it can be done like that, and that would probably be clearest.
  * Romain: I'm not sure I get which scenario the const added to the variadic get_value would break backwards compatibility. It's only saying to the compiler that the get_value isn't modifying the object.
  * Raphael: In case of the implementation, there's no visible change. In my understanding, most compilers would change the mangling of the function.
  * Romain: You're talking ABI changes?
  * Raphael: Yes.
  * Romain: I don't think this has been a concern for the interface.

* I finalized these changes in a pull request: `#593 <https://github.com/uxlfoundation/oneAPI-spec/pull/593>`__.
* For anyone who might be looking at it, I separated the pull request into 2 main components. There are several aspects of the current specification that could be improved (typos, etc.), which are not strictly related to this proposal. Those are all in the first commit (not content-changing). Second commit covers what we covered here. If you'd prefer two separate PRs, we can do that.

* Andrey: Currently these interfaces rely on vectors to pass multiple values around. Are there any plans to add support for std::span from C++20 instead of direct array?

  * Raphael: We wouldn't want to enable such types one-by-one; find a common trait attribute to any such type that would be enabled similarly to one another. We could probably use a SFINAE, converting them from one another.
  * Romain: That's only possible if minimum C++ version is C++20. As far as I know, it's only C++17. I don't think there are any plans to change the minimum version.
  * Andrey: If the client app is using C++20, can the span be enabled conditionally?
  * Raphael: Perhaps that could be an implementation choice, more than a specification decision.
  * Louise Hout: That could be an addition if there is value to add it. Probably more something to be considered if there is user feedback or something like that.
  * Romain: At least we have Andrey's feedback.
  * Andrey: My concern is that, for example, for strides, the size is usually known at compile time, so an array makes sense. It's nice not to require uses to incur the vector costs; span is just a suggestion.
  * Raphael: But it's a good one - thank you.

* Romain: I have a question as to the timeline of this. The specification request is up. We are working on things to make sure the Intel oneMKL 2025.0 product will be compatible with open source oneMKL interfaces. Will this change to the specification impact that?

  * Raphael: We've implemented these changes in Intel oneMKL 2025.0. No one expects implementation to change overnight, when specification changes. Though having the shortest gap between product and interface project is best.
  * Sarah Knepper: Intention is for the specification changes to be part of the 1.4 version of specification, the version that's coming up.
  * Raphael: In the meantime, any implementation would be at least partially specification abiding.

Conclusion:

* We've taken note of templating suggestions to make the type checks compile-time checks, and I think it's very valuable to consider. Timeline-wise, not confident this can be done in very near future, but it has been noted.

Updates from last meeting - Sarah Knepper:

oneMKL Specification:

* There were some new distributions added for RNG, plus a few other extensions and bug fixes were made. There are also some improvements to sparse BLAS.
* There was a very long, good discussion on the programmatic versions enabling. That was as part of an RFC/implementation and so, for instance, to say that the BLAS domain in the oneMKL element of the specification supports version oneAPI 1.3, whatever revision, you would define this ONEMKL_BLAS_SPEC_VERSION with a value of 103. I think other elements of the specification are doing similarly to programmatically be able to tell what version of the specification an implementation supports.
* There are a couple open pull requests; one for sparse BLAS, adding a sorted by rows property. And Raphael just discussed the type safety-motivated changes and other corrections for discrete Fourier transforms.

oneMKL Interfaces:

* Great work has been done on completing all of the tasks that were wanting to be done in Q3 and Q4 this year for the Open Source checklist. That included introducing an RFC - Request for Comment- process, adding "help wanted" label to open issues to showcase our wish list of how folks in the community can help contribute, documentation of our project maintainer roles and responsibilities and how folks can become one.
* Using the newly-introduced RFC process, there is an RFC about oneMKL interface renaming, which has also had some really great discussion. It's going to be wrapping up soon.
* The sparse BLAS implementation updated the oneMKL backends to match the new sparse API we've talked about in previous Math SIG meetings.
* The portBLAS implementation had some generic device and initial support added, and similar changes are being made to portFFT.
* Under the category of showcasing performance portability, the oneMKL interfaces were successfully built and run on a Grace Hopper machine on the Bede cluster at Durham University, which has an Arm host CPU and an NVIDIA GPU. All the computations were done on the NVIDIA GPU and it was compiled with a version of DPC++ that was built with Arm host CPU support. So this is awesome work, showcasing that the interfaces project works with an Arm host.

oneAPI DevSummit:

* Hopefully you are all aware or maybe are even giving a talk at the oneAPI Dev Summit on October 9th and 10th. If you haven't registered yet, I definitely recommend doing that, since there are a lot of great talks. I pulled up a couple that seemed a little more relevant to the Math SIG folks, including one on GROMACS and another on Ginkgo.

This is our last scheduled Math SIG for the year, though if anyone has any pressing topics they would like to bring before next year, we can create another meeting for that.
